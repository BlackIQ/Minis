package com.shahriar;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Signup implements ActionListener {
    String fullname, fa, sa;
    int a, b, c;
    boolean h;

    //create frame
    JFrame frame;

    //create button
    JButton button;

    //create all textfields
    JTextField name;
    JTextField firstaddress;
    JTextField secondaddress;
    JTextField age;
    JTextField Height;
    JTextField Weight;

    public Signup(){

    }


    public void setupAndShowFrame(){

        //build frame
        frame = new JFrame("Signup Form");
        frame.setVisible(true);
        frame.setSize(350, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        frame.setLayout(null);
    }

    public void setAndShowButton(){
        //build textfields
        //full name
        name = new JTextField();
        name.setBounds(25, 30, 280, 30);
        frame.add(name);

        //first address
        firstaddress = new JTextField();
        firstaddress.setBounds(25, 100, 280, 30);
        frame.add(firstaddress);

        //second address
        secondaddress = new JTextField();
        secondaddress.setBounds(25, 170, 280, 30);
        frame.add(secondaddress);

        //age
        age = new JTextField();
        age.setBounds(25, 240, 280, 30);
        frame.add(age);

        //Height
        Height = new JTextField();
        Height.setBounds(25, 310, 280, 30);
        frame.add(Height);

        //Weight
        Weight = new JTextField();
        Weight.setBounds(25, 380, 280, 30);
        frame.add(Weight);

        //-------------------------------------------------------------------
        // submit button

        button = new JButton("submit");
        button.setBounds(80, 480, 160, 40);
        frame.add(button);
        button.addActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        fullname = name.getText();
        fa = firstaddress.getText().toLowerCase();
        sa = secondaddress.getText().toLowerCase();
        a = Integer.parseInt(age.getText());
        b = Integer.parseInt(Height.getText());
        c = Integer.parseInt(Weight.getText());


        //show all data entry
        System.out.println("Your registration details:");
        System.out.println();
        //full name
        if (fullname.length() >= 3){
            System.out.println("name: " + fullname);
        }else{
            System.out.println("ERROR! The name entered must be at least three characters long.");
        }

        System.out.println();

        // address
        h = !fa.equals(sa);
        if (h){
            System.out.println("first address: " + fa);
            System.out.println();
            System.out.println("second address: " + sa);
        }else{
            System.out.println("ERROR! The addresses entered must not be the same");
        }

        System.out.println();

        //age
        if (a >= 18){
            System.out.println("Age: " + a);
        }else{
            System.out.println("ERROR! You must be 18 years old or older.");
        }

        System.out.println();

        //Height
        if (b >= 100){
            System.out.println("Height: " + b);
        }else{
            System.out.println("ERROR! Your height should be 100 and above.");
        }

        System.out.println();

        //Weight
        if (c >= 40){
            System.out.println("Weight: " + c);
        }else{
            System.out.println("ERROR! The weight entered must be 40 or more.");
        }

    }
}
