using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace wcf_chat
{
    // ПРИМЕЧАНИЕ. Команду "Переименовать" в меню "Рефакторинг" можно использовать для одновременного изменения имени класса "ServiceChat" в коде и файле конфигурации.
    //реализация интерфейса 
    //описываем как все будет делаться 
    //после каждого подключения создается экземпляр сервиса, это нужно исправить
    //теперь все подключающиеся будут работать с одним сервисом
    [ServiceBehavior(InstanceContextMode =InstanceContextMode.Single)]

    public class ServiceChat : IServiceChat
    {
        //список в котором хранится информация о пользователях
        List<ServerUser> users = new List<ServerUser>();
        //будем использовать для генерации айдишников
        int nextId = 1;

        public int Connect(string name)
        {
            //создаем нового юзера 
            ServerUser user = new ServerUser()
            {
                ID = nextId,
                Name = name,
                operationContext = OperationContext.Current
            };
            //увеличиваем id для следующего пользователя
            nextId++;

            //выводим сообщение о подключении нового пользователя
            SendMsg(": " + user.Name + " подключился к чату!", 0);

            //добавляем нового пользователя в список
            users.Add(user);

            return user.ID;
        }

        public void Disconnect(int id)
        {
            //находим пользователя, который хочет отключиться 
            var user = users.FirstOrDefault(i => i.ID == id);
            //если нашли его, удаляем
            if (user != null)
            {
                users.Remove(user);
                //выводим сообщение об отключении пользователя
                SendMsg(": " + user.Name + " отключился от чата!", 0);
            }

        }

        public void SendMsg(string msg, int id)
        {
            //перебираем всех пользователей 
            foreach (var item in users)
            {
                //формируем ответ сервера

                string answer = DateTime.Now.ToShortTimeString();   //время

                //находим пользователя
                var user = users.FirstOrDefault(i => i.ID == id);
                if (user != null)
                {
                    answer += ": " + user.Name + " ";
                }

                //добавляем само сообщение
                answer += msg;

                //отправка сооющения 
                item.operationContext.GetCallbackChannel<IServiceChatCallBack>().MsgCallBack(answer);
            }
        }
    }
}
