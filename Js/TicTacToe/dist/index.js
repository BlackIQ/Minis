"use strict";
const input = require('prompt-sync')();
const SIZE = 3;
var Player;
(function (Player) {
    Player["none"] = "-";
    Player["X"] = "X";
    Player["O"] = "O";
})(Player || (Player = {}));
class Place {
    constructor(placement) {
        this.symbol = Player.none;
        this.placement = placement;
    }
    setSymbol(symbol) {
        this.symbol = symbol;
    }
}
let winner = Player.none;
function initBoard() {
    let board = [];
    let count = 0;
    for (let i = 0; i < SIZE; i++) {
        board.push([]);
        for (let j = 0; j < SIZE; j++) {
            board[i].push(new Place(count));
            count++;
        }
    }
    return board;
}
function printBoard(board) {
    let str = "";
    for (let i = 0; i < board.length; i++) {
        let str2 = "";
        str += " ";
        for (let j = 0; j < board[i].length; j++) {
            str += " " + board[i][j].symbol + " ";
            str2 += " " + (board[i][j].placement + 1) + " ";
            str += j === board[i].length - 1 ? "" : "|";
            str2 += j === board[i].length - 1 ? "" : "|";
        }
        str += "\t " + str2;
        str += board.length - 1 !== i ? "\n-------------\t-------------\n" : "";
    }
    console.log(str);
}
function playerTurn(board, player) {
    const MIN_INPUT = 0;
    const MAX_INPUT = 8;
    const place = input("Enter colomn (1-9) -> ") - 1;
    console.log("");
    if (place === -1) {
        console.log("exit");
        process.exit(1);
    }
    if (place > MAX_INPUT || place < MIN_INPUT || isNaN(place)) {
        console.log("input is not in invalid");
        return playerTurn(board, player);
    }
    else {
        let row = Math.floor(place / board.length), col = Math.floor(place % board.length);
        if (board[row][col].symbol === Player.none) {
            board[row][col].setSymbol(player);
            return board;
        }
        else {
            console.log("place is already taken!");
            return playerTurn(board, player);
        }
    }
}
function checkIfWin(board) {
    const allEqual = (arr) => arr.every(v => v.symbol === arr[0].symbol && v.symbol !== Player.none);
    let col1 = [], col2 = [], col3 = [], diag1 = [], diag2 = [];
    for (let row = 0; row < board.length; row++) {
        diag1.push(board[row][row]);
        diag2.push(board[board.length - row - 1][row]);
        col1.push(board[row][0]);
        col2.push(board[row][1]);
        col3.push(board[row][2]);
        if (allEqual(board[row])) {
            return board[row][0].symbol;
        }
    }
    let all = [col1, col2, col3, diag1, diag2];
    for (const list of all) {
        if (allEqual(list)) {
            return list[0].symbol;
        }
    }
    return Player.none;
}
function checkTie(board) {
    for (const row of board) {
        for (const col of row) {
            if (col.symbol == Player.none) {
                return;
            }
        }
    }
    console.log("\n***\nits a tie!\n***\n");
    process.exit(1);
}
let board = initBoard();
console.log("\n*******************************\n this is a game of tic tac toe,\n in your turn enter the number of\n the place you want to put your symbol at.\n to exit in middle enter 0 or nothing\n*******************************\n");
while (winner === Player.none) {
    printBoard(board);
    console.log("\n *** X turn ***\n");
    board = playerTurn(board, Player.X);
    winner = checkIfWin(board);
    if (winner !== Player.none)
        break;
    printBoard(board);
    checkTie(board);
    console.log("\n *** O turn ***\n");
    board = playerTurn(board, Player.O);
    winner = checkIfWin(board);
}
console.log("\n");
printBoard(board);
let statment = "";
statment = winner === Player.X ? "\n***\nplayer X won!\n***\n" : "\n***\nplayer O won!\n***\n";
console.log(statment);
//# sourceMappingURL=index.js.map