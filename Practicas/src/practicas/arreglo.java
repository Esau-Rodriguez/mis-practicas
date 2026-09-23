/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package practicas;

/**
 *
 * @author PC-01
 */
public class arreglo {

    public static void main(String[] args) {
        int[] numeros = new int[6];
        numeros[0] = 10;
        numeros[1] = 20;
        numeros[2] = 30;

        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Posición: " + i + " : " + numeros[i]);
        }
    }
}
