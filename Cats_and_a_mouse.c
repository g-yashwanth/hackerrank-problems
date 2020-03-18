char* catAndMouse(int x, int y, int z) {
    static char cat_a[] = "Cat A";
    static char cat_b[] = "Cat B";
    static char mouse_c[] = "Mouse C";
    int m_a=z-x,m_b=z-y;
    if(z-x<0)
        m_a=-(z-x);
    if(z-y<0)
        m_b=-(z-y);
    if(x==y || m_a==m_b){
        return mouse_c;
    }else if(m_a>m_b){
        return cat_b;
    }else {
        return cat_a;
    }

}
