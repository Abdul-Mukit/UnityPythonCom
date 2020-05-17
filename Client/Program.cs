using NetMQ;
using NetMQ.Sockets;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace zmq_test
{
    class Program
    {

        string[] buffer;
        public float tx, ty, tz, roll, pitch, yaw;

        static void Main(string[] args)
        {
            Program p = new Program();

            for (int i = 0; i < 10; i++)
            {
               p.RunRequestSocket();
            }
            Console.ReadKey();

        }

        public void RunRequestSocket()
        {
            using (var client = new RequestSocket())
            {
                client.Connect("tcp://localhost:5555");
                client.SendFrame("Send Pose");
                var msg = client.ReceiveFrameString();
                //Console.WriteLine("From Server: {0}", msg);
                buffer = msg.Split(',');

                tx = (float)Convert.ToDouble(buffer[0]);
                ty = (float)Convert.ToDouble(buffer[1]);
                tz = (float)Convert.ToDouble(buffer[2]);
                roll = (float)Convert.ToDouble(buffer[3]);
                pitch = (float)Convert.ToDouble(buffer[4]);
                yaw = (float)Convert.ToDouble(buffer[5]);

                Console.WriteLine("tx: " + tx);
                Console.WriteLine("ty: " + ty);
                Console.WriteLine("tz: " + tz);
                Console.WriteLine("roll: " + roll);
                Console.WriteLine("pitch: " + pitch);
                Console.WriteLine("yaw: " + yaw);
            }
        }
    }
}
