using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ServiceModel;

namespace ChatHost
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //чтобы реализовавылся интерфейс диспоуз у нашего объекта типа ServiceHost, когда он нам будет уже не нужен и все ресурсы освобождались 
            using (var host = new ServiceHost(typeof(wcf_chat.ServiceChat)))
            {
                host.Open();//открываем хост
                Console.WriteLine("Хост стартовал!");
                Console.ReadLine();//чтобы приложение не закрылось
            }
        }
    }
}
