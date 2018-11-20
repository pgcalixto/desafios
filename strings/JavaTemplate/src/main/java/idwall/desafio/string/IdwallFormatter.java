package idwall.desafio.string;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Rodrigo Catão Araujo on 06/02/2018.
 */
public class IdwallFormatter extends StringFormatter {

    public IdwallFormatter(Integer limit, Boolean justify) {
        super(limit, justify);
    }

    /**
     * Formats text, with no justify, for the lines to meet the column cap as
     * defined in the object instantiation.
     *
     * @param text Text to be formatted.
     * @return Formatted text.
     */
    @Override
    public String format(String text) {
        List<String> lines = this.getFormattedLines(text);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < lines.size() - 1; ++i) {
            sb.append(lines.get(i));
            sb.append("\n");
        }
        sb.append(lines.get(lines.size() - 1));

        return sb.toString();
    }

    /**
     * Format lines (without justify) and return them in a list of lines.
     *
     * @param text Text to be formatted
     * @return List of already formatted lines
     */
    private List<String> getFormattedLines(String text) {

        List<String> lines = new ArrayList<String>();

        // The regexp below splits the words separated by whitespace, but keeps
        // the "\n" split as a single word.
        // "Hello\n\n  World" would result in a ["Hello", "\n", "\n", "World"].
        String[] words = text.split(" |((?<=\n)|(?=\n))");

        StringBuilder sb = new StringBuilder();
        int lineLength = 0;
        for (String w : words) {
            if (w.equals("\n")) {
                // when "\n", add the current built string to the list and reset
                lines.add(sb.toString());
                sb.setLength(0);
                lineLength = 0;
            }
            else if (lineLength == 0) {
                // beginning of line
                sb.append(w);
                lineLength += w.length();
            }
            else if (lineLength + w.length() + 1 <= 40) {
                // word does not overflow line
                sb.append(' ' + w);
                lineLength += w.length() + 1;
            }
            else {
                // word overflows line
                lines.add(sb.toString());
                sb.setLength(0);
                sb.append(w);
                lineLength = w.length();
            }
        }
        // add last built string to the list and return
        lines.add(sb.toString());
        return lines;
    }
}
