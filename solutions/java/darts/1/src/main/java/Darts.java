class Darts {
    int score(double x, double y) {
        double d2 = x * x + y * y;
        
        return d2 <= 1 ? 10 :
               d2 <= 25 ? 5 :
               d2 <= 100 ? 1 : 0;
    }
}
