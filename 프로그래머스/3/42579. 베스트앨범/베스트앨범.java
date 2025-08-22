import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genreTotal = new HashMap<>();
        Map<String, List<int[]>> info = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            genreTotal.put(genres[i], genreTotal.getOrDefault(genres[i], 0) + plays[i]);
            
            info.putIfAbsent(genres[i], new ArrayList<>());
            info.get(genres[i]).add(new int[]{i, plays[i]});
        }
        
        List<String> genreTitle = new ArrayList<>(genreTotal.keySet());
        genreTitle.sort((a, b) -> genreTotal.get(b) - genreTotal.get(a));
        
        List<Integer> result = new ArrayList<>();
        for (String genre : genreTitle) {
            List<int[]> songs = info.get(genre);
            
            songs.sort((a, b) -> {
                if (a[1] == b[1]) return a[0] - b[0];
                return b[1] - a[1];
            });
            
            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                result.add(songs.get(i)[0]);
            }
            
        }
        return result.stream().mapToInt(i -> i).toArray();
    }
}