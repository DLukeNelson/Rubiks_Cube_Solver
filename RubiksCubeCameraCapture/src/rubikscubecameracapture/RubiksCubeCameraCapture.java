package rubikscubecameracapture;

import javax.swing.*;

public class RubiksCubeCameraCapture extends JFrame {
    
    JLabel img_wob_ex = new JLabel(""),
            img_yrg_ex = new JLabel(""),
            filler = new JLabel("");
    
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
        this.pack();
    }
    
    private void init() {
        this.img_wob_ex.setIcon(createImageIcon("wob.png", 
                "White Orange Blue"));
        this.img_yrg_ex.setIcon(createImageIcon("yrg.png",
                "Yellow Red Green"));
        this.add(img_wob_ex).setBounds(0, 0, 500, 500);
        this.add(img_yrg_ex).setBounds(500, 0, 500, 500);
        this.add(filler);
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
}
