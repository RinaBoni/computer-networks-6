using System;
using System.Net;
using System.Net.Sockets;

namespace netchat
{
    internal class Program
    {
        static void Main(string[] args)
        {
            const string ip = "127.0.0.1"; //стандартный localhost адрес
            const int port = 8080;

            //IPAddress.Parse(ip) помогает преобразовать строку в стандартный формат для IP адреса
            //end point место подключения. У одного сервера их может быть несколько разного вида, к нему смогут подключаться по разным адресам
            var tcpEndPoint = new IPEndPoint(IPAddress.Parse(ip), port);

            //сокет это "дверь" через которое будет устанавливаться соединение
            //1 - использование IPv4. 2 - потоковая передача данных для протокола tcp. 3 - указываем что используем протокол tcp
            var tcpSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            //далее нужно выполнить связывание, т.е. перевести сокет в режим ожидания: указать ему конкретный порт, который он должен слушать 
            tcpSocket.Bind(tcpEndPoint);
            //запускаем сокет для прослушивания. здесь мы можем задать очередь подключения, те когда на один и тот же могут пытаться подключаться несколько колиентов (в данном случае будет выстраиваться очередь клиентов)
            tcpSocket.Listen(5);

            //делаем процесс прослушивания (он должен быть бесконечным, поэтому используем конструкцию while(true)
            while (true)
            {

            }
        }
    }
}
