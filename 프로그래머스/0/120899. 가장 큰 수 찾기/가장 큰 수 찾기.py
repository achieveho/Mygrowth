def solution(array):
    m = max(array)
    m_idx = array.index(max(array))
    
    return [m, m_idx]