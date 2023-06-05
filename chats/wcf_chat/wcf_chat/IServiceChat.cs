using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace wcf_chat
{
    // ПРИМЕЧАНИЕ. Можно использовать команду "Переименовать" в меню "Рефакторинг", чтобы изменить имя интерфейса "IServiceChat" в коде и файле конфигурации.
    //интерфейс
    //описание того что может делать сервис
    //описанные здесь мктоды будут теми рычагами, которыми будет пользоваться юзер  работая с сервером 
    //здесь пишем основной функционал 
    //ServiceContract говорит о том что этот интерфейс будет предоставлять собой договоренночть как пользователь
    //будет взаимодействовать с сервисом и у каждого метода в этом интерфейсе, с помощью которых мы будем
    //взаимодействовать с сервисом со сторонв клиента должен быть атрибут  OperationContract. Т.е. метод, у которого есть этод атрибут будет виден со стороны клиента
    [ServiceContract(CallbackContract =typeof(IServiceChatCallBack))]
    public interface IServiceChat
    {
        //подключеник к сервису
        [OperationContract]
        int Connect(string name);


        //отключение от сервиса (сервису прилетает сообщение что такого клиента больше нет 
        //id - id отключившегося клиента
        [OperationContract]
        void Disconnect(int id);


        [OperationContract(IsOneWay = true)]
        void SendMsg(string msg, int id);
    }

    public interface IServiceChatCallBack
    {
        //возвращает сообщение нашим клиентам
        [OperationContract(IsOneWay =true)]
        void MsgCallBack(string msg);
    }
}
