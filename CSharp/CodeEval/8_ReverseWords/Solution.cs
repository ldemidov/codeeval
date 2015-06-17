using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeEval._8_ReverseWords
{
    class Solution : ISolution
    {

        public void Execute(string[] args)
        {
            using (StreamReader reader = File.OpenText(args[0]))
                while (!reader.EndOfStream)
                {
                    string line = reader.ReadLine();
                    if (null == line)
                        continue;
                    // do something with line
                    Console.WriteLine(
                        string.Join(" ", line.Trim().Split(' ').Reverse().ToArray())
                        );
                }
        }

    }
}
