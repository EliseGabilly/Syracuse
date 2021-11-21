# Syracuse
Personal project to illustrate of the extention of the Syracuse conjecture.

The Syracuse conjecture is also kown as : 3n + 1 problem, the 3n + 1 conjecture, the Ulam conjecture, Kakutani's problem, the Thwaites conjecture, Hasse's algorithm, the Syracuse problem or the Collatz conjecture.
The function is f(n)=n/2 if (mod2) else f(n)=3n+1. The conjecture say that for any starting n the runtine will end at 1.

The extention of the Syracuse conjecture define the problem as :
For many a and b the function f(n)=n/2 or f(n)=a*n+b
The routine will start to loop.


This python project use matplotlib and numpy to illustrate the flying time and other value for the conjecture.
A console menu give multiple option on how to run it :
  - One function of form ax+b
      - Show the plot
      - Save the plot as an image
      - Use default (a=3, b=1, size=10)
      - Input a, b and size
  - Multiple function (every function with a and b between 1 and a given size)
      - Range for a and b
      - Size tested for every function
      - Save recap plot
      - Save every undividual plot

Individual plot will have an output of the form :
![alt text](https://github.com/EliseGabilly/Syracuse/blob/master/main_img/explanation.jpg)
  - The title is a reminder of a, b and size
  - How to read heatmap : top left case refer to 1 to right refer to size (here 10)
    example : in the 9th column, 3rd row the flying time correspond to f(29) as 9+(3-1)*10 = 29 (10 beeing the size)
  -  I   - Flying time :
  - II  - Highest value :
  - III - Stoping value :
  - IV  - Flying time plot :
  - V   - Highest value plot :
  - VI  - Written data :

Multipl recap will output 1 visual data recap of the form :
![alt text](https://github.com/EliseGabilly/Syracuse/blob/master/main_img/visualDataRecap_10_10.jpg)
And, is the range for a/b is >= 10, 6 recap of the form : (refer to individual plot for explanation)
Flying time ![alt text](https://github.com/EliseGabilly/Syracuse/blob/master/main_img/recapFlying_10_10.jpg)
Highest value ![alt text](https://github.com/EliseGabilly/Syracuse/blob/master/main_img/recapHighest_10_10.jpg)
Stoping value ![alt text](https://github.com/EliseGabilly/Syracuse/blob/master/main_img/recapStoping_10_10.jpg)
Flying time plot ![alt text](https://github.com/EliseGabilly/Syracuse/blob/master/main_img/recapFlyingPlot_10_10.jpg)
Highest value plot ![alt text](https://github.com/EliseGabilly/Syracuse/blob/master/main_img/recapHighestPlot_10_10.jpg)
Written data ![alt text](https://github.com/EliseGabilly/Syracuse/blob/master/main_img/recapData_10_10.jpg)

