import javax.swing.*;
import java.awt.event.ItemEvent;
import java.io.IOException;

public class PDf2TXT_GUI extends JFrame{
    //define instance variable
    private static String inPath;
    private static String outPath;
    private static String convertDirectory;

    // this actually does the GUI program itself
    public static void main(String[] args){
        // create the window itself
        JFrame window = new JFrame();
        window.setSize(500, 350);
        window.setLayout(null);
        window.setLocationRelativeTo(null);
        window.setName(".pdf to .txt converter graphical version 0.2.0");

        //create the label at the top to introduce the program
        JLabel intro = new JLabel("This program runs PDF2TXT graphically.");
        intro.setBounds(125, 25, 450, 20);
        window.add(intro);

        //create the entry fields for the input and output file paths
        //infile
        JTextField infile = new JTextField("input file path");
        infile.setBounds(50, 75, 400, 20);
        window.add(infile);
        //this action serves to record the entry file path
        infile.addActionListener(e -> inPath = infile.getText());

        //outfile
        JTextField outfile = new JTextField("output file path");
        outfile.setBounds(50, 125, 400, 20);
        window.add(outfile);
        //this one records the output file path
        outfile.addActionListener(e -> outPath = outfile.getText());


        //create a checkbox for whole file or partial file conversion
        JCheckBox wholeFile = new JCheckBox("Convert whole directory?");
        wholeFile.setBounds(152, 175, 300, 20);
        window.add(wholeFile);
        //this checks the state of the checkbox. if it's checked, we convert the entire directory
        wholeFile.addItemListener(e -> {
            if(e.getStateChange() == ItemEvent.SELECTED)
                convertDirectory = " -d ";
            else
                convertDirectory = " -f ";
        });

        // the run button to execute the program
        JButton run = new JButton("Run PDF2TXT");
        run.setBounds(160, 225, 150, 20);
        window.add(run);
        // this will happen when the run button is pressed.
        run.addActionListener(e -> {
            String runScript = ("bash ./wrapper " + convertDirectory + " " + inPath + " -o " + outPath);
            try {
                Runtime.getRuntime().exec(runScript);
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        });

        // make the completed window visible
        window.setVisible(true);
    }
}
