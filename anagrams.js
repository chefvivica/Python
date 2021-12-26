const anagrams = (s1, s2) =>{
    const count = {}
    for ( let i of s1){
        if(!char in count){
            count[s1[char]] = 1
        }
        count[s1[char]] += 1
    }

    for ( let i of s2){
        if(count[s2[i]] == undefined){
            return false;
        }else{
            count[s2[i]] -= 1;
        }
    }

    for(let i in count){
        if(count[i] != 0){
            return false;
        }
    }
    
    return true

}

console.log(anagrams('cats', 'tocs'))