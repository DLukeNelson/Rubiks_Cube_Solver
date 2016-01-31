package rubikscubecameracapture;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.*;

public class RubiksCubeCameraCapture extends JFrame {

    JLabel img_wob_ex = new JLabel(""),
            img_yrg_ex = new JLabel(""),
            filler = new JLabel("");
    JButton execute_action = new JButton("Do Magic"),
            open_action = new JButton("Open Stuff");

    public static void main(String[] args) {
        RubiksCubeCameraCapture rccc
                = new RubiksCubeCameraCapture("Rubiks Cube Camera Capture");
    }

    public RubiksCubeCameraCapture(String title) {
        super(title);
        this.setVisible(true);
        this.setEnabled(true);
        this.setDefaultCloseOperation(3);
        this.setExtendedState(this.getExtendedState() | JFrame.MAXIMIZED_BOTH);
        this.init();
        //this.pack();
    }

    private void init() {
        this.img_wob_ex.setIcon(createImageIcon("wob.png",
                "White Orange Blue"));
        this.img_yrg_ex.setIcon(createImageIcon("yrg.png",
                "Yellow Red Green"));
        this.add(img_wob_ex).setBounds(20, 20, 500, 500);
        this.add(img_yrg_ex).setBounds(1280 - 520, 20, 500, 500);
        this.add(execute_action).setBounds(1280 / 2 - 50, 580, 100, 20);
        this.add(open_action).setBounds(1280 / 2 - 50, 540, 100, 20);
        this.add(filler);

        open_action.addActionListener(new ActionListenerImpl());
    }

    protected ImageIcon createImageIcon(String path,
            String description) {
        java.net.URL imgURL = getClass().getResource(path);
        if (imgURL != null) {
            return new ImageIcon(imgURL, description);
        } else {
            System.err.println("Couldn't find file: " + path);
            return null;
        }
    }

    private static class ActionListenerImpl implements ActionListener {

        public ActionListenerImpl() {
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            try {
                JFrame infojf = new JFrame("Information");
                JLabel infojfinfo = new JLabel("Name your image containing the"
                        + "white side \"wob.png\" and your yellow side \"yrg.png\"");
                infojf.add(infojfinfo);
                infojf.setVisible(true);
                infojf.setEnabled(true);
                infojf.pack();
                boolean success = (new File("C:\\$cube.solver\\")).mkdirs();
                assert(!success):("Unable to create a dir");
                Runtime.getRuntime().exec("Explorer.exe \"C:\\$cube.solver\\\"");
            } catch (IOException ex) {
                Logger.getLogger(RubiksCubeCameraCapture.class.getName()).log(Level.SEVERE, null, ex);
            }
        }

    }
}
