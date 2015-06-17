using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeEval._9_StackImplementation
{
    /* https://www.codeeval.com/open_challenges/9/
     * Write a program which implements a stack interface for integers. The interface should have ‘push’ and ‘pop’ functions. Your task is to ‘push’ a series of integers and then ‘pop’ and print every alternate integer.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains a series of space delimited integers, one per line.

For example:


1
2
1 2 3 4
10 -2 3 4
OUTPUT SAMPLE:

Print to stdout every alternate space delimited integer, one per line.

For example:


1
2
4 2
4 -2
*/
    public class Solution : ISolution
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
                    var ints = line.Split(' ').Select(int.Parse);
                    var stack = new Stack<int>();
                    var output = new List<int>();
                    foreach (var i in ints)
                    {
                        stack.Push(i);
                    }

                    while (stack.Count > 0)
                    {
                        output.Add(stack.Pop());

                        if(stack.Count > 0)
                            stack.Pop();
                    }
                    Console.WriteLine(string.Join(" ", output));
                }
        }
    }
}
