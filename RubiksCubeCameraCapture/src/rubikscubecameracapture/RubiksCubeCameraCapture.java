package rubikscubecameracapture;

import javax.swing.JFrame;

public class RubiksCubeCameraCapture extends JFrame {

    public static void main(String[] args) {
        RubiksCubeCameraCapture rccc
                = new RubiksCubeCameraCapture("Rubiks Cube Camera Capture");
    }
    
    public RubiksCubeCameraCapture (String title){
        super(title);
        this.setVisible(true);
        this.setEnabled(true);
        this.setDefaultCloseOperation(3);
        this.setExtendedState(this.getExtendedState() | JFrame.MAXIMIZED_BOTH);
        this.init();
    }
    
    private void init(){
        
    }
}
