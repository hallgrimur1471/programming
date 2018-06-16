/* Modify the temperature conversion program to print a heading
 * above the table. */

#include <stdio.h>

/* print Fahreinheit-Celsius table
 * for fahr = 0, 20, ..., 300 */
main()
{
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;      /* lower limit of temperature table */
    upper = 300;    /* upper limit */
    step = 20;      /* step size */

    printf("%-15s%-15s\n", "Fahrenheit", "Celsius");
    fahr = lower;
    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%7.0f %13.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
