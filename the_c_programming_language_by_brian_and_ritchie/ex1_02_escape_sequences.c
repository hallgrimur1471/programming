/* Experiment to find out what happens when printf's argument
 * string contains \c, where c is some character not listed above.*/

#include <stdio.h>

main()
{
    printf("a hello\aworld\n");
    printf("b hello\bworld\n");
    printf("c hello\cworld\n");
    printf("d hello\dworld\n");
    printf("e hello\eworld\n");
    printf("f hello\fworld\n");
    printf("g hello\gworld\n");
    printf("h hello\hworld\n");
    printf("i hello\iworld\n");
    printf("j hello\jworld\n");
    printf("k hello\kworld\n");
    printf("l hello\lworld\n");
    printf("m hello\mworld\n");
    printf("n hello\nworld\n");
    printf("o hello\oworld\n");
    printf("p hello\pworld\n");
    printf("q hello\qworld\n");
    printf("r hello\rworld\n");
    printf("s hello\sworld\n");
    printf("t hello\tworld\n");
    //printf("u hello\uworld\n");
    printf("v hello\vworld\n");
    printf("w hello\wworld\n");
    printf("x hello\x91world\n");
    printf("y hello\ycworld\n");
    printf("z hello\zcworld\n");
}
