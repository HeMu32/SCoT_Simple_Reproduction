def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    
    pattern_to_color = {}
    
    for pattern, color in zip(patterns, colors):
        if pattern not in pattern_to_color:
            pattern_to_color[pattern] = color
        elif pattern_to_color[pattern] != color:
            return False
    
    return True