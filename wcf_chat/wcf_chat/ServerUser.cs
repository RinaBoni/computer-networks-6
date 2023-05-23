using System.ServiceModel;


namespace wcf_chat
{
    internal class ServerUser
    {
        public int ID { set; get; }

        public string Name { set; get; }

        public OperationContext operationContext { set; get; }
    }
}
