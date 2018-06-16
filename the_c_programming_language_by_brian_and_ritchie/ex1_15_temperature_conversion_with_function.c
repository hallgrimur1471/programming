/* Rewrite the temperature conversion program of Section 1.2 to
 * use a function for conversion. */

#include <stdio.h>

float fahr2celsius(float fahr);

main()
{
  float fahr, celsius;
  int lower, upper, step;

  lower = 0; /* lower limit of temperature table */
  upper = 300; /* upper limit */
  step = 20; /* step size */

  fahr = lower;
  while (fahr <= upper) {
    celsius = fahr2celsius(fahr);
    printf("%3.0f %6.1f\n", fahr, celsius);
    fahr = fahr + step;
  }
}

float fahr2celsius(float fahr)
{
  return (5.0/9.0) * (fahr-32.0);
}
