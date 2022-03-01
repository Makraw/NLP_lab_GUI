import javax.swing.*;
import java.awt.event.ActionListener;

public class PDf2TXT_GUI {
    public static void Window(){
        // create the window itself
        JFrame window = new JFrame();
        window.setSize(500, 350);
        window.setLayout(null);

        // create the label at the top to introduce the program
        JLabel intro = new JLabel("This program runs PDF2TXT graphically.");
        intro.setBounds(110, 25, 450, 20);
        window.add(intro);

        // create the entry fields for the input and output file paths
        // infile
        JTextField infile = new JTextField("input file path");
        infile.setBounds(50, 75, 400, 20);
        window.add(infile);

        //outfile
        JTextField outfile = new JTextField("output file path");
        outfile.setBounds(50, 125, 400, 20);
        window.add(outfile);

        //create a checkbox for whole file or partial file conversion
        JCheckBox wholeFile = new JCheckBox("Convert whole directory?");
        wholeFile.setBounds(130, 175, 300, 20);
        window.add(wholeFile);

        // the run button to execute the program
        JButton run = new JButton("Run PDF2TXT");
        run.setBounds(160, 225, 150, 20);
        window.add(run);

        // make the completed window visible
        window.setVisible(true);
    }

    public static void main(String[] args){
        Window();
    }
}
