using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using ChatClient.ServiceChat;

namespace ChatClient
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window, IServiceChatCallback
    {
        //поддключен ли на данный момент наш клиент к серверу или нет 
        bool isConnected = false;
        //создаем объект типа нашего хоста в клиенте чтоюы мы могли взаимодействовать с его методами
        ServiceChatClient client;
        //id клиента
        int ID;
        
        public MainWindow()
        {
            InitializeComponent();
        }

        //при загрузке окна выделяется память под клиета
        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            
        }

        //подключаем пользователя
        void ConnectUser()
        {
            if(!isConnected)
            {
                client = new ServiceChatClient(new System.ServiceModel.InstanceContext(this));
                ID = client.Connect(tbUserName.Text);//присваиваем клиенту имя, Connect возвращает id
                tbUserName.IsEnabled = false; //при подключении блокируем изменение ника
                bConnDiscon.Content = "Disconnect";
                isConnected = true;
            }
        }

        //отключаем пользователя
        void DisconnectUser()
        {
            if (isConnected)
            {
                client.Disconnect(ID);
                client = null;  
                tbUserName.IsEnabled = true;    //при отключении даем редактировать ник
                bConnDiscon.Content = "Connect";
                isConnected = false;
            }
        }
        
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            if(isConnected)
            {
                DisconnectUser();
            }
            else
            {
                ConnectUser();
            }
        }

        //возвращает сообщение нашим клиентам
        public void MsgCallBack(string msg)
        {
            //каждый раз, когда сервер юудет присылать сообщение, оно будет выводиться в listbox
            lbChat.Items.Add(msg);
            lbChat.ScrollIntoView(lbChat.Items[lbChat.Items.Count-1]);
        }

        //при закрытии окна крестиком, отключаем пользователя
        private void Window_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            DisconnectUser() ;
        }

        //при нажатии на enter отправляем сообщение
        private void tbMessage_KeyDown(object sender, KeyEventArgs e)
        {
            if(e.Key == Key.Enter)
            {
                if(client!= null)   //если человек законектился, отправляем сообщение
                {
                    client.SendMsg(tbMessage.Text, ID);
                    tbMessage.Text = string.Empty;//после отправки сообщения очищаем tb
                }
                
            }
        }
    }
}
