from collections import defaultdict
from typing import Dict, List, Set, Tuple

test_cases = [
    (
        (
            "abcyy",
            2,
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
        ),
        7,
    ),
    (
        ("azbk", 1, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
        8,
    ),
    (
        (
            "mttrflecxwguvtqewhnuyipfgogruikbvewevpxtuemfrhhrheuoknifjdnuutxmilwdjczkegqhdyzeouxcqzrlnwssnacgfjffmtbudjkrcvmbpidrmznscieqodbdstxrgfxcwrscvqasjvzouhqssoveiogqjzunhjzrjszlldqgviufithydgvofybggxcesqudogjsbctclfeequcgfolntbxbeewnyusnjndfqpqeijjzssncywboahysbufscpnmcqfxonpywiaecjgayqsinonbizkrurltczrxzgyxyxggsgwthcurtwsvvmtnxcuvggftbdklaktnpwmqxuwmkehrhqcriczntjrszskusatzusnjtulmvettzpttpaojlwefcqjvbxwxdhpcflqtdnwihfqkebybmlosabzxndkwukwzlkhhadzedrefmkyhylbamqgkmarecwmfacvsclqvxjqpafzwanxyhnupncoqbiodtpvfyukdrmardudvaowpyotfhevnmhtjqilrfkvrvtebrfbwhhwvznwzxiyxbnwkksgzzzpdovjapahucghlvrnwycciportayczbatydqilhuaclqaldcupactjkuigpwazjgbweqyoxyrccxrpshmajqjlplcjsyuiypkyzixbussqrpvahpqodolzpvaxujjceozzixazhsmddyckxlivzoqsxvkkjamdejxvobqxlpxmjoqvbxxeecgijuuxsbvnqsdqkwzhhcbwpsrukfsouetbsokmbeljyacyzlxrqtwldpmcubhgbprrutebunvavhaxiqymdrhiljmibbulaeqabcawqihlaqrqxaxycsutnkltdsjmxvupdaeghqfajrzsjzguwrrbimwhqvfhtuzeeppkgmmeyklnxdsnwoqlijstlactpddodtqqldqghhmzwuwsljkiwrfjgjetytklnlaudigzwvtxszangtfgnhgkqbtxdtybcrdrzsqpzzymoanugrhdbfwuormcmnzafhpmipesykaibhhixqmxrnudotbhvqowvifmrxrlhqhmbtfpzhnntjswjjpxqgudqhcrmkonajjnqpjuvfbjrsmwvketrzrrkrzfzdqqpadllhngeziphbfxocnqddaitutdgfdrfdrxrklndzfqykwsxxcyfyjirmsiqrisbqidujiewndwcdxbezckkutarxkiiwkufvlqqfbaoptvxywldaqajfdqrrhncbscddoptrhxjxfqilobljvyyzhwsqkhltesjzpdxqhhbmenpkwboeftoyyfvpipwagmackcayoqfshsbygltwxqzqognnwhlrniffmvxikyqyoapbwypeuuxauulisppjxdysmchwfnvjjhpqitcyzgglxvkkwlapaioayaxhdijlmnxkudinriqvkofvukhrghuprdaxibrkocrqgmxkdkdmyczkarterixtkapoutmdrxwrmxthsvsxigkjpikgocdsvqonsupayhhgbdocdxytmultkntjkiysptrsbvnsnipbwsvotlfipwvskkknwovhhnqhhzxbmnfbpmkbqlsnkkymrroisbpmiioxjgxrmfnwfpqfehiewxpwxzndcijxzzmntrpibsbznnsflakjykywswpzaogwlamtugnfkkbaufhmqzozcvyudkiuivabgeveluuzsngxrirsxfrwhtzgtsvnjzduywalepsuxvamdecippjwxoerkytfwpryhkdezbvgyevpclzibfqxrmsllfeljtmxmawkkvghqgzruyuukodjrbvjesddebewnfqwobqetzrghtpqdcpeslnruoeiwlhxavmqehnarihpcndmazjzkbpfedqamcgyjwdzhpfvewndedgsrgxkbuosgatyukoypytrevbhgwwchvgaznpqjzvzpzbjnuhuovmpryupwbznzkgvfvgucrcbwpwahzduluklfqwpdqshzhqzrxlgohmnlznrtfbwishdrvpdspjpyabbmqwsvmwxjkpyysnqxzlslzhifvhspakgktfytflronusmifktqqnvqkjgghwqcouhmjgcxlwwioknduovyayyqmvbbzmjbkzwembhtacaicbfqukanwudxegelqnonoaqhwtwcvfusjzqpgssiesjjucpqxkgyhljsmphtzotvrhjiwzjvushumezxsyiukkrzrzjzumnkjoyawurtfqtflsqemvpugeqnrepktktwncneorthcaauvpyvvrdjzhvytpkpitiaciiqgypqcfxdifvypdawovlkzzhfxmfkizhbbofuawikmxbtysqwrmhknbagavqvequzykamtziccodwoitvvzkhunnxxfnuilrqnsylrbuirwsgqcxcfberiuprulkmyhmcanraqqnalatnkvxojxlrabgxciduhkeerjrjotbwtugoxpekaxsfoprbgrgvkjcgjihqlxuoquhhdhteocztpcdcypgtinvrpwzjgqnahcytkljjsbjzspoyphbbmymnffzaxcjdhasntgmruzjvxbrpjzphuxxnfdehyvuqvtnojzephoanjmmkukmjpywwdeobhiqmdh",
            8662,
            [
                10,
                8,
                8,
                24,
                15,
                5,
                21,
                12,
                13,
                10,
                14,
                21,
                3,
                11,
                14,
                11,
                18,
                16,
                14,
                11,
                3,
                22,
                12,
                12,
                24,
                16,
            ],
        ),
        843743849,
    ),
]


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1

        for _ in range(t):
            next_char_count = [0] * 26
            
            # Process each character in the alphabet
            for i in range(26):
                if char_count[i] == 0:
                    continue
                
                # Calculate how many of each character will be produced
                count = char_count[i]
                transform_length = nums[i]
                
                # Add the transformed characters to the next count
                for j in range(1, transform_length + 1):
                    next_index = (i + j) % 26  # Handle wrapping around
                    next_char_count[next_index] = (next_char_count[next_index] + count)
            
            # Update for the next transformation
            char_count = next_char_count
        

        return sum(char_count) % (10**9 + 7)


if __name__ == "__main__":
    solver = Solution()
    for i, case in enumerate(test_cases):
        inputs, n_expected = case
        s, t, nums = inputs
        n_counted = solver.lengthAfterTransformations(s, t, nums)
        try:
            assert n_expected == n_counted
            print(f"Test Case [{i}]: PASSED")
        except AssertionError:
            print(f"Test Case [{i}]: FAILED. Expected {n_expected}. Returned {n_counted}")
