using System;

class Team
{
    public int attack;
    public int defend;
    public Random random = new Random();

    public Team()
    {
        this.attack = random.Next(0, 100);
        this.defend = random.Next(0, 100);
    }

    public Team(int attack)
    {
        this.attack = attack;
        this.defend = random.Next(0, 100);
    }

    public Team(int attack,int defend)
    {
        this.attack = attack;
        this.defend = defend;
    }
}
class Program
{
    static void Main(string[] args)
    {
        Random random = new Random();
        Team Blue = new Team();
        Team Red = new Team();
        int BlueScore = 0, RedScore = 0;

        for(int i = 0; i <= 10; i++)
        {
            int first = random.Next(0,2);
            Blue.attack = random.Next(0, 100);
            Red.attack = random.Next(0, 100);

            if (first == 0)
            {
                if (Blue.attack >= Red.defend)
                {
                    Console.WriteLine($"Blue won!\nBlue:{Blue.attack} --> Red:{Red.defend}");
                    BlueScore++;
                }

                else
                {
                    Console.WriteLine($"Red won!\nRed:{Red.defend} --> Blue:{Blue.attack}");
                    RedScore++;
                }
            }

            else
            {
                if (Red.attack >= Blue.defend)
                {
                    Console.WriteLine($"Red won!\nRed:{Red.attack} --> Blue:{Blue.defend}");
                    RedScore++;
                }

                else
                {
                    Console.WriteLine($"Blue won!\nBlue:{Blue.defend} --> Red:{Red.attack}");
                    BlueScore++;
                }
            }
        }
        if (BlueScore > RedScore)
            Console.WriteLine($"Blue won!\n{BlueScore}-{RedScore}");

        else
            Console.WriteLine($"Red won!\n{RedScore}-{BlueScore}");
    }
}