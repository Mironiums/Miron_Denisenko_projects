package Chess;



public class Pawn extends Piece {

    public Pawn(String color, int[] position) {
        super(color, position);
    }

    public boolean move(int[] whereTo, Piece[][] field) {

        boolean flag = false;
        if (super.getColor().equals("white")) {
            if (super.getPosition()[0] + 1 == whereTo[0] && (super.getPosition()[1] + 1 == whereTo[1] || super.getPosition()[1] - 1 == whereTo[1])) {
                if (field[whereTo[0]][whereTo[1]] != null) {
                    if (field[whereTo[0]][whereTo[1]].getColor().equals("black")) {
                        flag = true;
                    }
                }
            } else if (super.getPosition()[0] == 1) {
                if (super.getPosition()[0] + 1 == whereTo[0] && super.getPosition()[1] == whereTo[1]) {
                    if (field[whereTo[0]][whereTo[1]] == null) {
                        flag = true;
                    }
                } else if (super.getPosition()[0] + 2 == whereTo[0] && super.getPosition()[1] == whereTo[1]) {
                    if (field[whereTo[0]][whereTo[1]] == null && field[whereTo[0] - 1][whereTo[1]] == null) {
                        flag = true;
                    }
                }
            } else{
                if (super.getPosition()[0] + 1 == whereTo[0] && super.getPosition()[1] == whereTo[1]) {
                        if (field[whereTo[0]][whereTo[1]] == null) {
                            flag = true;
                        }
                }
            }
        } else{
            if (super.getPosition()[0] - 1 == whereTo[0] && (super.getPosition()[1] + 1 == whereTo[1] || super.getPosition()[1] - 1 == whereTo[1])) {
                if (field[whereTo[0]][whereTo[1]] != null) {
                    if (field[whereTo[0]][whereTo[1]].getColor().equals("white")) {
                        flag = true;
                    }
                }
            } else if (super.getPosition()[0] == 6) {
                if (super.getPosition()[0] - 1 == whereTo[0] && super.getPosition()[1] == whereTo[1]) {
                    if (field[whereTo[0]][whereTo[1]] == null) {
                        flag = true;
                    }
                } else if (super.getPosition()[0] - 2 == whereTo[0] && super.getPosition()[1] == whereTo[1]) {
                    if (field[whereTo[0]][whereTo[1]] == null && field[whereTo[0] +1][whereTo[1]] == null) {
                        flag = true;
                    }
                }
            } else{
                if (super.getPosition()[0] - 1 == whereTo[0] && super.getPosition()[1] == whereTo[1]) {
                    if (field[whereTo[0]][whereTo[1]] == null) {
                        flag = true;
                    }
                }
            }
        }
        return flag;
    }



    public String toString() {
        if (super.getColor().equals("white")) {
            return "♙";
        }else {
            return "♟";
        }
    }
}
