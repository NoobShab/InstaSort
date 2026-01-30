#ifndef ANALYZER_H
#define ANALYZER_H

#include <string>
#include <vector>
#include <unordered_map>
#include "reel.h"

struct HashtagStats{
    long long totalViews = 0;
    long long totalLikes = 0;
    long long totalComments = 0;
    long long engagementScore = 0;
    int reelCount = 0;
};

namespace Analyze {
        std::unordered_map<std::string, HashtagStats>
        rankHashtagsByEngagement(const std::vector<Reel>& reels);
};

#endif