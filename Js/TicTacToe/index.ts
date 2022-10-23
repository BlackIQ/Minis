
/**
 * created by matanton have fun!
 */

const input = require('prompt-sync')();


const SIZE = 3; // size of one side of board
enum Player{
    none = "-", // 0
    X = "X", // 1
    O = "O" // 2
}


class Place {
    placement:number;
    symbol = Player.none;
    constructor(placement:number){
        this.placement = placement;
    }

    /**
     * setSymbol
     */
    public setSymbol(symbol:Player) {
        this.symbol = symbol;
    }
}


let winner = Player.none;

/**
 * initializes the board with the places
 * @param board the board of the game
 */
function initBoard():Place[][]{
    let board:Place[][] = [];
    let count = 0;
    
    for (let i = 0; i < SIZE; i++){
        board.push([]);
        for (let j = 0; j < SIZE; j++) {
            board[i].push(new Place(count));
            count++;
        }
    }
    return board;
}


/**
 * prints the tictactoe board in a user friendly way with
 * '-' as not taken 'x' as x player place and 'o' as o player place
 * @param board the tictactoe board
 */
function printBoard(board: Place[][]){
    let str = "";
    for(let i = 0; i < board.length; i++){
        let str2 = "";
        str += " ";
        for(let j = 0; j < board[i].length; j++){
            // add the value of the board at the current position
            str += " " + board[i][j].symbol + " ";
            str2 += " " + (board[i][j].placement + 1) + " ";
            // add '|' if it's not the last column 
            str += j === board[i].length - 1 ? "" : "|";
            str2 += j === board[i].length - 1 ? "" : "|";
        }
        str += "\t " + str2;
        // add space between lines if not last line
        str += board.length - 1 !== i ? "\n-------------\t-------------\n": "";
    }
    console.log(str);
}


/**
 * makes a players turn, gets input of placement and puts the coresponding 
 * charicter in it
 * @param board 3x3 integer array
 * @param player player x o or none
 * @returns updated board
 */
function playerTurn(board: Place[][], player: Player): Place[][]{
    const MIN_INPUT = 0;
    const MAX_INPUT = 8;
    // get and check placement 
    const place:number = input("Enter colomn (1-9) -> ") - 1;
    console.log("");
    // exit if input is 0
    if (place === -1){
        console.log("exit");
        process.exit(1);
    }
    // if not in place recurse to get correct placement
    if (place > MAX_INPUT || place < MIN_INPUT || isNaN(place)){
        console.log("input is not in invalid");
        return playerTurn(board, player);
    }
    else{ 
        let row = Math.floor(place / board.length),
        col = Math.floor(place % board.length); // convert 1d index to 2d index
        // check if place is taken
        if (board[row][col].symbol === Player.none){
            board[row][col].setSymbol(player); // set place with new symbol
            return board;
        }
        else{
            console.log("place is already taken!");
            return playerTurn(board, player);
        }
    }
}

/**
 * checks if any row colomn or diagonal is the same symbol
 * meaning someone won
 * @param board game board
 * @returns the player type that won (none if no win)
 */
function checkIfWin(board: Place[][]): Player{
    // checks if all elements are equal (and not 0)
    const allEqual = (arr: Place[]) => arr.every(v => v.symbol === arr[0].symbol && v.symbol !== Player.none); 
    
    let col1 = [], col2 = [], col3 = [], diag1 = [], diag2 = [];
    // get all rows and colomns and diagonals to checks
    for(let row = 0; row < board.length; row++){
        diag1.push(board[row][row]); // diagonal left to right
        diag2.push(board[board.length - row - 1][row]); // diagonal right to left
        col1.push(board[row][0]); // every colomn
        col2.push(board[row][1]);
        col3.push(board[row][2]);
        if (allEqual(board[row])) { // every row
            return board[row][0].symbol;
        }
    }
    let all = [col1, col2, col3, diag1, diag2];
    for (const list of all) {
        if (allEqual(list)){
            return list[0].symbol;
        }
    }
    return Player.none;
}

/**
 * check if board is filled, if so then exit game
 * @param board game board
 */
function checkTie(board:Place[][]) {
    for (const row of board){
        for (const col of row){
            if (col.symbol == Player.none){
                return;
            }
        }
    }
    console.log("\n***\nits a tie!\n***\n");
    process.exit(1);
}


let board = initBoard();
// instructions                                 
console.log("\n*******************************\n this is a game of tic tac toe,\n in your turn enter the number of\n the place you want to put your symbol at.\n to exit in middle enter 0 or nothing\n*******************************\n");
// game loop
while (winner === Player.none){
    // init
    printBoard(board);
    console.log("\n *** X turn ***\n");
    // player 1 turn
    board = playerTurn(board, Player.X);
    // check if player won
    winner = checkIfWin(board);
    if (winner !== Player.none) break;
    printBoard(board);
    checkTie(board);
    
    // player 2 turn
    console.log("\n *** O turn ***\n");
    board = playerTurn(board, Player.O);
    // check if player won
    winner = checkIfWin(board);

}
console.log("\n");
printBoard(board);
let statment = "";
statment = winner === Player.X ? "\n***\nplayer X won!\n***\n" : "\n***\nplayer O won!\n***\n";
console.log(statment);

