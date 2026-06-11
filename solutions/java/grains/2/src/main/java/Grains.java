import java.math.BigInteger;

class Grains {

    BigInteger grainsOnSquare(final int square) {
        if (square > 0 && square < 65){
            return BigInteger.ONE.shiftLeft(square - 1);    
        }
        throw new IllegalArgumentException("square must be between 1 and 64");
    }

    BigInteger grainsOnBoard() {
        return BigInteger.ONE.shiftLeft(64).subtract(BigInteger.ONE);
    }

}
