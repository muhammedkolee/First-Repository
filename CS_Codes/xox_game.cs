using System;

namespace Xox
{
    class Program
    {
        public static char[] arr = { '1', '2', '3', '4', '5', '6', '7', '8', '9' };
        public static char secim;
        public static int sira = 0;
        public static bool oyun = false;
        public static int win = 2;
        static void Main(string[] args)
        {
            while (!oyun)
            {
                if (sira == 0)
                {
                    Board();
                    Console.WriteLine("PLAYER 1 OYNUYOR!");
                    secim = Convert.ToChar(Console.ReadLine());
                    Hamle();
                    if (Check() == 1)
                    {
                        win = 1;
                        oyun = true;
                    }
                    if (Check() == -1)
                    {
                        Console.Clear();
                        Board();

                        sira = 2;
                        Console.WriteLine("OYUNCULAR BERABERE");
                        break;
                    }
                }
                else if (sira == 1)
                {
                    Board();
                    Console.WriteLine("PLAYER 2 OYNUYOR!");
                    secim = Convert.ToChar(Console.ReadLine());
                    Hamle();
                    if (Check() == 1)
                    {
                        win = 0;
                        oyun = true;
                    }
                    if (Check() == -1) 
                    {
                        Console.Clear();
                        Board();
                        sira = 2;
                        Console.WriteLine("OYUNCULAR BERABERE");
                        break;
                    }
                }
            }
            if (win == 1)
            {
                Console.WriteLine("OYUN BİTTİ!\nKAZANAN:PLAYER 1");
                Board();
            }
            else if (win == 0)
            {
                Console.WriteLine("OYUN BİTTİ!\nKAZANAN:PLAYER 2");
                Board();
            }
            Console.ReadKey();
        }
        public static void Hamle()
        {
            for (int i = 0; i <= arr.Length - 1; i++)
            {
                if (arr[Convert.ToInt32(Convert.ToString(secim)) - 1] == 'X' || (arr[Convert.ToInt32(Convert.ToString(secim)) - 1] == 'O'))
                {
                    Console.Clear();
                    Console.WriteLine("Bu kutu daha önce zaten seçildi, tekrar deneyiniz.");
                    break;
                }
                else if (arr[i] == secim)
                {
                    if (sira == 0)
                    {
                        Console.Clear();
                        arr[i] = 'X';
                        sira = 1;
                        break;
                    }
                    else if (sira == 1)
                    {
                        Console.Clear();
                        arr[i] = 'O';
                        sira = 0;
                        break;
                    }
                }
            }
        }
        public static int Check()
        {
            if (arr[0] == arr[1] && arr[1] == arr[2]) return 1;

            else if (arr[3] == arr[4] && arr[4] == arr[5]) return 1;

            else if (arr[6] == arr[7] && arr[7] == arr[8]) return 1;

            else if (arr[0] == arr[4] && arr[4] == arr[8]) return 1;

            else if (arr[2] == arr[4] && arr[4] == arr[6]) return 1;

            else if (arr[0] == arr[3] && arr[3] == arr[6]) return 1;

            else if (arr[1] == arr[4] && arr[4] == arr[7]) return 1;

            else if (arr[2] == arr[5] && arr[5] == arr[8]) return 1;

            else if ((arr[0] == 'X' || arr[0] == 'O') && (arr[1] == 'X' || arr[1] == 'O') && (arr[2] == 'X' || arr[2] == 'O') && (arr[3] == 'X' || arr[3] == 'O') && (arr[4] == 'X' || arr[4] == 'O') && (arr[5] == 'X' || arr[5] == 'O') && (arr[6] == 'X' || arr[6] == 'O') && (arr[7] == 'X' || arr[7] == 'O') && (arr[8] == 'X' || arr[8] == 'O')) return -1;

            else return 0;
        }
        public static void Board()
        {
            Console.WriteLine("    |    |    |");
            Console.WriteLine(" {0}  | {1}  |  {2} |", arr[0], arr[1], arr[2]);
            Console.WriteLine("    |    |    |");
            Console.WriteLine("---------------");
            Console.WriteLine("    |    |    |");
            Console.WriteLine(" {0}  | {1}  |  {2} |", arr[3], arr[4], arr[5]);
            Console.WriteLine("    |    |    |");
            Console.WriteLine("---------------");
            Console.WriteLine("    |    |    |");
            Console.WriteLine(" {0}  | {1}  |  {2} |", arr[6], arr[7], arr[8]);
            Console.WriteLine("    |    |    |");
        }
    }
}