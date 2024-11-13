
import java.io.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) throws Exception {
        // Press Opt+Enter with your caret at the highlighted text to see how
        // IntelliJ IDEA suggests fixing it.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i < t; i++){
            int n = Integer.parseInt(br.readLine()); // 입력받음
            String school = "";
            int drink = 0;
            for (int j = 0; j < n; j++){
                final String[] array = br.readLine().split(" ");
                if (Integer.parseInt(array[1]) > drink){
                    drink = Integer.parseInt(array[1]);
                    school = array[0];

                }
            }
            sb.append(school).append("\n");
        }

        System.out.print(sb);
    }
}