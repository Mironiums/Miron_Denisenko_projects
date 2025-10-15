package Chess;


public class Bishop extends Piece {


    public Bishop(String color, int[] position) {
        super(color, position);
    }


    public boolean move(int[] whereTo, Piece[][] field) {

        boolean flag = true;

        if (whereTo[0]>super.getPosition()[0] && whereTo[1]>super.getPosition()[1]) {
            for(int i=0;i<whereTo[1]-super.getPosition()[1] -1;i++) {
                if (field[super.getPosition()[0]+i][super.getPosition()[1]+i] != null) {
                    flag = false;
                }
            }
        } else if(whereTo[0]<super.getPosition()[0] && whereTo[1]<super.getPosition()[1]) {
            for(int i=0;i<super.getPosition()[1]-whereTo[1] -1;i++) {
                if (field[super.getPosition()[0]-i][super.getPosition()[1]-i] != null) {
                    flag = false;
                }
            }
        } else if(whereTo[0]>super.getPosition()[0] && whereTo[1]<super.getPosition()[1]) {
            for(int i=0;i<super.getPosition()[1]-whereTo[1] -1;i++) {
                if (field[super.getPosition()[0]+i][super.getPosition()[1]-i] != null) {
                    flag = false;
                }
            }
        } else if (whereTo[0]<super.getPosition()[0] && whereTo[1]>super.getPosition()[1]) {
            for(int i=0;i<whereTo[1]-super.getPosition()[1] -1;i++) {
                if (field[super.getPosition()[0]-i][super.getPosition()[1]+i] != null) {
                    flag = false;
                }
            }
        } else{
            flag=false;
        }
        if (flag && (field[whereTo[0]][whereTo[1]] != null)){

            try {
                if (field[whereTo[0]][whereTo[1]].getColor().equals(super.getColor())) {
                    flag = false;
                }
            }catch (Exception e){
                flag = false;
            }
        }

        return flag;
    }


    public String toString(){
        if (super.getColor().equals("white")) {
            return "♗";
        }else {
            return "♝";
        }
    }
}
