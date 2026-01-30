#include "analyzer.h"

std::unordered_map<std::string, HashtagStats>
Analyze::rankHashtagsByEngagement(const std::vector<Reel>& reels){
    std::unordered_map<std::string, HashtagStats> table;
    // const std::vector<Reel>& reels,
    // const std::string& hashtag) {
        //     std::vector<Reel> result;
        
        for(const auto& r : reels){
            auto& stats = table[r.hashtag];

            stats.totalViews += r.views;
            stats.totalLikes += r.likes;
            stats.totalComments += r.comments;

            stats.engagementScore += r.likes + (2 * r.comments);
            stats.reelCount++;
        }
        
        return table;
    }

struct EmergingHashtags {
    std::string hashtag;
    double emergenceScore;
    HashtagStats stats;
};
  
std::vector<EmergingHashtags> Analyze :: getTopEmergingHashtags(
    const std::unordered_map
)