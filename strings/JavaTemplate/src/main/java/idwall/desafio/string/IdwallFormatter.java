package idwall.desafio.string;

/**
 * Created by Rodrigo Catão Araujo on 06/02/2018.
 */
public class IdwallFormatter extends StringFormatter {

    /**
     * Should format as described in the challenge
     *
     * @param text
     * @return
     */
    @Override
    public String format(String text) {

        // The regexp below splits the words separated by whitespace, but keeps
        // the "\n" split as a single word.
        // "Hello\n\n  World" would result in a ["Hello", "\n", "\n", "World"].
        String[] words = text.split(" |((?<=\n)|(?=\n))");

        StringBuilder sb = new StringBuilder();
        int lineLength = 0;
        for (String w : words) {
            // If word is "\n", reset line length. Otherwise, if line is empty,
            // add word. Otherwise, if new word does not overflow line, add
            // whitespace + word. Otherwise, insert a new line and add word.
            if (w.equals("\n")) {
                lineLength = 0;
            }
            else if (lineLength == 0) {
                lineLength += w.length();
            }
            else if (lineLength + w.length() + 1 <= 40) {
                lineLength += w.length() + 1;
                sb.append(' ');
            }
            else {
                lineLength = w.length();
                sb.append('\n');
            }
            sb.append(w);
        }
        return sb.toString();
    }
}
