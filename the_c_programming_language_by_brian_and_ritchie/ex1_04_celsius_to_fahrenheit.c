/* Write a program to print the corresponding Celsius to Fahrenheit
 * table. */

#include <stdio.h>

/* print Celsius-Fahrenheit table
 * for celsius = -20, 0, ..., 160 */
main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = -20;      /* lower limit of temperature table */
    upper = 160;    /* upper limit */
    step = 20;      /* step size */

    printf("%-15s%-15s\n", "Celsius", "Fahrenheit");
    celsius = lower;
    while (celsius <= upper) {
        fahr = ((9.0/5.0) * celsius) + 32.0;
        printf("%7.0f %13.1f\n", celsius, fahr);
        celsius = celsius + step;
    }
}
