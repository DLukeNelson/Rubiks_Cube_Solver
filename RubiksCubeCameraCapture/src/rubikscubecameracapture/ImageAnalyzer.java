/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rubikscubecameracapture;

import java.awt.Color;
import java.awt.GraphicsConfiguration;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import static javax.swing.Spring.height;
import static javax.swing.Spring.width;

public class ImageAnalyzer {

    File wobf, yrgf, wobtf, yrgtf;
    BufferedImage wob, yrg, wobt, yrgt;

    public ImageAnalyzer() throws IOException {
        wobf = new File("C:\\$cube.solver\\wob.png");
        yrgf = new File("C:\\$cube.solver\\yrg.png");

        wob = ImageIO.read(wobf);
        yrg = ImageIO.read(yrgf);

        wobt = new BufferedImage(500, 500, BufferedImage.TYPE_INT_ARGB);
        yrgt = new BufferedImage(500, 500, BufferedImage.TYPE_INT_ARGB);

        boolean success = (new File("C:\\$cube.solver\\$8fe3e821a\\")).mkdirs();
        assert (!success) : ("Unable to create a dir");

        wobt = filter(wob, "white");
        wobt = filter(wob, "orange");
        wobt = filter(wob, "blue");
        wobt = filter(wob, "yellow");
        wobt = filter(wob, "red");
        wobt = filter(wob, "green");
        wobtf = new File("C:\\$cube.solver\\$8fe3e821a\\wobn.png");
        ImageIO.write(wobt, "png", wobtf);
    }

    private BufferedImage filter(BufferedImage inimage, String filter) {
        BufferedImage outimage = wobt;
        if (filter.equals("white")) {
            for (int i = 0; i < inimage.getHeight(); i++) {
                for (int j = 0; j < inimage.getWidth(); j++) {
                    int rgb = inimage.getRGB(i, j);
                    //System.out.println(rgb);
                    float hsb[] = new float[3];
                    int r = (rgb >> 16) & 0xFF;
                    int g = (rgb >> 8) & 0xFF;
                    int b = (rgb) & 0xFF;
                    Color.RGBtoHSB(r, g, b, hsb);
                    if (hsb[1] < 0.2 && hsb[2] <= 1) {
                        outimage.setRGB(i, j, Color.white.getRGB());
                    }
                }
            }
            //System.out.println(Color.blue.getRGB());
        } else if (filter.equals("orange")) {
            for (int i = 0; i < inimage.getHeight(); i++) {
                for (int j = 0; j < inimage.getWidth(); j++) {
                    int rgb = inimage.getRGB(i, j);
                    //System.out.println(rgb);
                    float hsb[] = new float[3];
                    int r = (rgb >> 16) & 0xFF;
                    int g = (rgb >> 8) & 0xFF;
                    int b = (rgb) & 0xFF;
                    Color.RGBtoHSB(r, g, b, hsb);
                    float deg = hsb[0] * 360;
                    if (deg >= 15 && deg < 50 &&(hsb[2] > 0.4 && hsb[1] > 0.5)) {
                        outimage.setRGB(i, j, Color.orange.getRGB());
                    }
                }
            }
            //System.out.println(Color.blue.getRGB());
        } else if (filter.equals("blue")) {
            for (int i = 0; i < inimage.getHeight(); i++) {
                for (int j = 0; j < inimage.getWidth(); j++) {
                    int rgb = inimage.getRGB(i, j);
                    //System.out.println(rgb);
                    float hsb[] = new float[3];
                    int r = (rgb >> 16) & 0xFF;
                    int g = (rgb >> 8) & 0xFF;
                    int b = (rgb) & 0xFF;
                    Color.RGBtoHSB(r, g, b, hsb);
                    float deg = hsb[0] * 360;
                    if (deg >= 210 && deg < 270 &&(hsb[2] > 0.2)) {
                        outimage.setRGB(i, j, Color.blue.getRGB());
                    }
                }
            }
        } else if (filter.equals("yellow")) {
            for (int i = 0; i < inimage.getHeight(); i++) {
                for (int j = 0; j < inimage.getWidth(); j++) {
                    int rgb = inimage.getRGB(i, j);
                    //System.out.println(rgb);
                    float hsb[] = new float[3];
                    int r = (rgb >> 16) & 0xFF;
                    int g = (rgb >> 8) & 0xFF;
                    int b = (rgb) & 0xFF;
                    Color.RGBtoHSB(r, g, b, hsb);
                    float deg = hsb[0] * 360;
                    if (deg >=  50 && deg <  90 &&(hsb[2] > 0.5)) {
                        outimage.setRGB(i, j, Color.gray.getRGB());
                    }
                }
            }
        } else if (filter.equals("red")) {
            for (int i = 0; i < inimage.getHeight(); i++) {
                for (int j = 0; j < inimage.getWidth(); j++) {
                    int rgb = inimage.getRGB(i, j);
                    float hsb[] = new float[3];
                    int r = (rgb >> 16) & 0xFF;
                    int g = (rgb >> 8) & 0xFF;
                    int b = (rgb) & 0xFF;
                    Color.RGBtoHSB(r, g, b, hsb);
                    float deg = hsb[0] * 360;
                    if (((deg > 0&&deg < 15)||(deg > 330))&&(hsb[2] < 1 && hsb[2] > 0.5)) {
                        outimage.setRGB(i, j, Color.red.getRGB());
                    }
                }
            }
        } else if (filter.equals("green")) {
            for (int i = 0; i < inimage.getHeight(); i++) {
                for (int j = 0; j < inimage.getWidth(); j++) {
                    int rgb = inimage.getRGB(i, j);
                    //System.out.println(rgb);
                    float hsb[] = new float[3];
                    int r = (rgb >> 16) & 0xFF;
                    int g = (rgb >> 8) & 0xFF;
                    int b = (rgb) & 0xFF;
                    Color.RGBtoHSB(r, g, b, hsb);
                    float deg = hsb[0] * 360;
                    if ((deg >=  90 && deg < 150)&&(hsb[2] > 0.2)) {
                        outimage.setRGB(i, j, Color.pink.getRGB());
                    }
                }
            }
        }
        return wobt;
    }

}
