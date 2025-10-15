package Chess;

import java.util.HashMap;
import java.util.Scanner;

public class chess {
    static void main(String[] args) {

        System.out.println("\n");
        System.out.println("Welcome to Chess");
        System.out.println("The game runs until you capture one of the kings, resignation or tie, because I haven't finished check and/or mate feature");
        System.out.println("The game runs by algebraic chess notation which looks like that: 'Pe2-e4' That line will move pawn from e2 to e4");
        System.out.println("Good luck. All the rules are explained, if you break something - it is your fault. Good luck");
        System.out.println("\n");

        Scanner input = new Scanner(System.in);
        Piece[][] field = new Piece[8][8];
        King[] kings = pregame_setup(field);


        String turn;
        int counter=0;
        String col_to_turn;
        int[] fromWhere=new int[2];
        int[] toWhere=new int[2];

        HashMap<String,Integer> board=new HashMap<>();
        board.put("a",0);
        board.put("b",1);
        board.put("c",2);
        board.put("d",3);
        board.put("e",4);
        board.put("f",5);
        board.put("g",6);
        board.put("h",7);

        boolean[] check=new boolean[2];
        boolean prev_check=false;

        do {
            if (counter%2.0 == 0){
                col_to_turn = "white";
            }else {
                col_to_turn = "black";
            }
            print_field(field,col_to_turn);
            if (check[0]){
                System.out.println("\nCheck on white\n");
            } else if(check[1]) {
                System.out.println("\nCheck on black\n");
            }
            System.out.print(col_to_turn+" to move\n> ");
            turn = input.nextLine().toLowerCase();
            fromWhere[1]=board.get(turn.substring(1,2));
            fromWhere[0]=Integer.parseInt(turn.substring(2,3))-1;
            toWhere[1]=board.get(turn.substring(4,5));
            toWhere[0]=Integer.parseInt(turn.substring(5,6))-1;

            if (turn.equals("resign")) {
                counter--;
                break;
            } else if (turn.equals("tie")) {
                System.out.println("\nDo you accept tie?\n> ");
                turn=input.nextLine().toLowerCase();
                if (turn.equals("yes")) {
                    break;
                }
            }

            if(field[fromWhere[0]][fromWhere[1]].getColor().equals(col_to_turn)) {
                if (field[fromWhere[0]][fromWhere[1]] instanceof Pawn && turn.charAt(0) == 'p') {
                    field[fromWhere[0]][fromWhere[1]].moving_process(toWhere,field,counter,    ((Pawn) field[fromWhere[0]][fromWhere[1]]) .move(toWhere, field));

                } else if (field[fromWhere[0]][fromWhere[1]] instanceof Rook && turn.charAt(0) == 'r') {
                    field[fromWhere[0]][fromWhere[1]].moving_process(toWhere,field,counter,     ((Rook) field[fromWhere[0]][fromWhere[1]]).move(toWhere, field));

                } else if(field[fromWhere[0]][fromWhere[1]] instanceof Bishop && turn.charAt(0) == 'b'){
                    field[fromWhere[0]][fromWhere[1]].moving_process(toWhere,field,counter,     ((Bishop) field[fromWhere[0]][fromWhere[1]]).move(toWhere, field));

                } else if(field[fromWhere[0]][fromWhere[1]] instanceof King && turn.charAt(0) == 'k'){
                    field[fromWhere[0]][fromWhere[1]].moving_process(toWhere,field,counter,     ((King) field[fromWhere[0]][fromWhere[1]]).move(toWhere, field));

                } else if(field[fromWhere[0]][fromWhere[1]] instanceof Knight && turn.charAt(0) == 'n'){
                    field[fromWhere[0]][fromWhere[1]].moving_process(toWhere,field,counter,     ((Knight) field[fromWhere[0]][fromWhere[1]]).move(toWhere, field));

                } else if(field[fromWhere[0]][fromWhere[1]] instanceof Queen && turn.charAt(0) == 'q'){
                    field[fromWhere[0]][fromWhere[1]].moving_process(toWhere,field,counter,     ((Queen) field[fromWhere[0]][fromWhere[1]]).move(toWhere, field));
                }
                else{
                    System.out.println("Invalid move");
                    counter--;
                }
            }else{
                System.out.println("Invalid move");
                counter--;
            }

            prev_check=check[0] || check[1];
            check=check(field,kings);

            counter++;
        }while(!turn.equals("resign") && findKing(field, kings));

    }


    static private King[] pregame_setup(Piece[][] field) {


        Rook w_r1 = new Rook("white", new int[]{0, 0});
        Rook w_r2 = new Rook("white", new int[]{0, 7});
        Rook b_r3 = new Rook("black", new int[]{7, 0});
        Rook b_r4 = new Rook("black", new int[]{7, 7});

        Knight w_n1 = new Knight("white", new int[]{0, 1});
        Knight w_n2 = new Knight("white", new int[]{0, 6});
        Knight b_n3 = new Knight("black", new int[]{7, 1});
        Knight b_n4 = new Knight("black", new int[]{7, 6});

        Bishop w_b1 = new Bishop("white", new int[]{0, 2});
        Bishop w_b2 = new Bishop("white", new int[]{0, 5});
        Bishop b_b3 = new Bishop("black", new int[]{7, 2});
        Bishop b_b4 = new Bishop("black", new int[]{7, 5});

        King w_k = new King("white", new int[]{0, 4});
        King b_k = new King("black", new int[]{7, 4});

        Queen w_q = new Queen("white", new int[]{0, 3});
        Queen b_q = new Queen("black", new int[]{7, 3});

        Pawn w_p1 = new Pawn("white", new int[]{1, 0});
        Pawn w_p2 = new Pawn("white", new int[]{1, 1});
        Pawn w_p3 = new Pawn("white", new int[]{1, 2});
        Pawn w_p4 = new Pawn("white", new int[]{1, 3});
        Pawn w_p5 = new Pawn("white", new int[]{1, 4});
        Pawn w_p6 = new Pawn("white", new int[]{1, 5});
        Pawn w_p7 = new Pawn("white", new int[]{1, 6});
        Pawn w_p8 = new Pawn("white", new int[]{1, 7});
        Pawn b_p9 = new Pawn("black", new int[]{6, 0});
        Pawn b_p10 = new Pawn("black", new int[]{6, 1});
        Pawn b_p11 = new Pawn("black", new int[]{6, 2});
        Pawn b_p12 = new Pawn("black", new int[]{6, 3});
        Pawn b_p13 = new Pawn("black", new int[]{6, 4});
        Pawn b_p14 = new Pawn("black", new int[]{6, 5});
        Pawn b_p15 = new Pawn("black", new int[]{6, 6});
        Pawn b_p16 = new Pawn("black", new int[]{6, 7});


        field[w_r1.getPosition()[0]][w_r1.getPosition()[1]] = w_r1;
        field[w_r2.getPosition()[0]][w_r2.getPosition()[1]] = w_r2;
        field[b_r3.getPosition()[0]][b_r3.getPosition()[1]] = b_r3;
        field[b_r4.getPosition()[0]][b_r4.getPosition()[1]] = b_r4;

        field[w_n1.getPosition()[0]][w_n1.getPosition()[1]] = w_n1;
        field[w_n2.getPosition()[0]][w_n2.getPosition()[1]] = w_n2;
        field[b_n3.getPosition()[0]][b_n3.getPosition()[1]] = b_n3;
        field[b_n4.getPosition()[0]][b_n4.getPosition()[1]] = b_n4;

        field[w_b1.getPosition()[0]][w_b1.getPosition()[1]] = w_b1;
        field[w_b2.getPosition()[0]][w_b2.getPosition()[1]] = w_b2;
        field[b_b3.getPosition()[0]][b_b3.getPosition()[1]] = b_b3;
        field[b_b4.getPosition()[0]][b_b4.getPosition()[1]] = b_b4;

        field[b_k.getPosition()[0]][b_k.getPosition()[1]] = b_k;
        field[w_k.getPosition()[0]][w_k.getPosition()[1]] = w_k;

        field[b_q.getPosition()[0]][b_q.getPosition()[1]] = b_q;
        field[w_q.getPosition()[0]][w_q.getPosition()[1]] = w_q;

        field[w_p1.getPosition()[0]][w_p1.getPosition()[1]] = w_p1;
        field[w_p2.getPosition()[0]][w_p2.getPosition()[1]] = w_p2;
        field[w_p3.getPosition()[0]][w_p3.getPosition()[1]] = w_p3;
        field[w_p4.getPosition()[0]][w_p4.getPosition()[1]] = w_p4;
        field[w_p5.getPosition()[0]][w_p5.getPosition()[1]] = w_p5;
        field[w_p6.getPosition()[0]][w_p6.getPosition()[1]] = w_p6;
        field[w_p7.getPosition()[0]][w_p7.getPosition()[1]] = w_p7;
        field[w_p8.getPosition()[0]][w_p8.getPosition()[1]] = w_p8;
        field[b_p9.getPosition()[0]][b_p9.getPosition()[1]] = b_p9;
        field[b_p10.getPosition()[0]][b_p10.getPosition()[1]] = b_p10;
        field[b_p11.getPosition()[0]][b_p11.getPosition()[1]] = b_p11;
        field[b_p12.getPosition()[0]][b_p12.getPosition()[1]] = b_p12;
        field[b_p13.getPosition()[0]][b_p13.getPosition()[1]] = b_p13;
        field[b_p14.getPosition()[0]][b_p14.getPosition()[1]] = b_p14;
        field[b_p15.getPosition()[0]][b_p15.getPosition()[1]] = b_p15;
        field[b_p16.getPosition()[0]][b_p16.getPosition()[1]] = b_p16;


        return new King[]{w_k, b_k};
    }


    public static void print_field(Piece[][] p, String color) {
        if (color.equals("black")) {
            for (int i = 0; i < 8; i++) {
                for (int j = 7; j >=0; j--) {
                    if (p[i][j] != null) {
                        System.out.print(p[i][j].toString());
                    } else {
                        if ((i + j) % 2.0 == 0) {
                            System.out.print("█");
                        } else {
                            System.out.print("  ");
                        }
                    }
                }
                System.out.println();
            }
        } else{
            for (int i = 7; i >=0 ; i--) {
                for (int j = 0; j < 8 ; j++) {
                    if (p[i][j] != null) {
                        System.out.print(p[i][j].toString());
                    } else {
                        if ((i + j) % 2.0 == 0) {
                            System.out.print("█");
                        } else {
                            System.out.print("  ");
                        }
                    }
                }
                System.out.println();
            }
        }
    }

    public static boolean findKing(Piece[][] p, King[] k) {
        boolean to_ret_w = false;
        boolean to_ret_b = false;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (p[i][j] == k[0]) {
                    to_ret_w=true;
                }
                if (p[i][j] == k[1]) {
                    to_ret_b=true;
                }
            }
        }
        return (to_ret_w && to_ret_b);
    }

    public static boolean[] check(Piece[][] phield ,King[] kings) {
        boolean check_on_white=false;
        boolean check_on_black=false;

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {

                        // From white to black

                if (phield[i][j] instanceof Pawn && phield[i][j].getColor().equals("white")) {
                    if(((Pawn) phield[i][j]).move(kings[1].getPosition() ,phield)){
                        check_on_black = true;
                    }
                } else if (phield[i][j] instanceof Rook && phield[i][j].getColor().equals("white")) {
                    if(((Rook) phield[i][j]).move(kings[1].getPosition() ,phield)){
                        check_on_black = true;
                    }
                } else if (phield[i][j] instanceof Bishop && phield[i][j].getColor().equals("white")) {
                    if(((Bishop) phield[i][j]).move(kings[1].getPosition() ,phield)){
                        check_on_black = true;
                    }
                }else if (phield[i][j] instanceof Queen && phield[i][j].getColor().equals("white")) {
                    if(((Queen) phield[i][j]).move(kings[1].getPosition() ,phield)){
                        check_on_black = true;
                    }
                }else if (phield[i][j] instanceof Knight && phield[i][j].getColor().equals("white")) {
                    if(((Knight) phield[i][j]).move(kings[1].getPosition() ,phield)){
                        check_on_black = true;
                    }

                    // From black to white

                }else if (phield[i][j] instanceof Pawn && phield[i][j].getColor().equals("black")) {
                    if(((Pawn) phield[i][j]).move(kings[0].getPosition() ,phield)){
                        check_on_white = true;
                    }
                } else if (phield[i][j] instanceof Rook && phield[i][j].getColor().equals("black")) {
                    if(((Rook) phield[i][j]).move(kings[0].getPosition() ,phield)){
                        check_on_white = true;
                    }
                } else if (phield[i][j] instanceof Bishop && phield[i][j].getColor().equals("black")) {
                    if(((Bishop) phield[i][j]).move(kings[0].getPosition() ,phield)){
                        check_on_white = true;
                    }
                } else if (phield[i][j] instanceof Queen && phield[i][j].getColor().equals("black")) {
                    if(((Queen) phield[i][j]).move(kings[0].getPosition() ,phield)){
                        check_on_white = true;
                    }
                } else if (phield[i][j] instanceof Knight && phield[i][j].getColor().equals("black")) {
                    if(((Knight) phield[i][j]).move(kings[0].getPosition() ,phield)){
                        check_on_white = true;
                    }
                }


            }
        }
        return new boolean[]{check_on_white, check_on_black};
    }

}
