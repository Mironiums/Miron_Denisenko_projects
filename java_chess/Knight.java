package Chess;

public class Knight extends Piece {

    public Knight(String color, int[] position) {
        super(color, position);
    }



    public boolean move(int[] whereTo, Piece[][] field) {

        boolean flag = false;

        if ( (super.getPosition()[0] +1 == whereTo[0] && super.getPosition()[1] +2 == whereTo[1]) || (super.getPosition()[0] +2 == whereTo[0] && super.getPosition()[1] +1 == whereTo[1]) || (super.getPosition()[0] -1 == whereTo[0] && super.getPosition()[1] -2 == whereTo[1]) || (super.getPosition()[0] -2 == whereTo[0] && super.getPosition()[1] -1 == whereTo[1]) || (super.getPosition()[0] +1 == whereTo[0] && super.getPosition()[1] -2 == whereTo[1]) || (super.getPosition()[0] +2 == whereTo[0] && super.getPosition()[1] -1 == whereTo[1]) || (super.getPosition()[0] -1 == whereTo[0] && super.getPosition()[1] +2 == whereTo[1]) || (super.getPosition()[0] -2 == whereTo[0] && super.getPosition()[1] +1 == whereTo[1]) ){
            if(field[whereTo[0]][whereTo[1]] == null || ! field[whereTo[0]][whereTo[1]].getColor().equals(super.getColor()) ) {
                flag = true;
            }
        }

        return flag;

    }




    public String toString() {
        if (super.getColor().equals("white")) {
            return "♘";
        }else {
            return "♞";
        }
    }
}
