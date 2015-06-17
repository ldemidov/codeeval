﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CodeEval._8_ReverseWords;


namespace CodeEval
{
    /*
     * https://www.codeeval.com/open_challenges/8/
     * Write a program which reverses the words in an input sentence.

INPUT SAMPLE:

The first argument is a file that contains multiple sentences, one per line. Empty lines are also possible.

For example:


1
2
Hello World
Hello CodeEval
OUTPUT SAMPLE:

Print to stdout each sentence with the reversed words in it, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces in each line you print.

For example:


1
2
World Hello
CodeEval Hello
*/
    class Program
    {
        static void Main(string[] args)
        {

            ISolution sln = new CodeEval._8_ReverseWords.Solution();
            
            sln.Execute(args);

        }
    }
}