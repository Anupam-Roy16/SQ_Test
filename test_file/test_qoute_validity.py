import pytest
import qoute_parsing_github_upload as QV

@pytest.mark.parametrize("qoute,status", [
("""SQ 123
If you have life air, you must use it for preaching.


His Holiness Jayapataka Swami
 20 Mar 2021
 Śrī Māyāpur, India""",True),
 ("""SQ 123
When Lord Caitanya Mahāprabhu asked Rāmānanda Rāya, “What is the greatest suffering that anyone can suffer in this world?” Rāmānanda Rāya said, “The suffering of a pure devotee for another pure devotee or the separation of a pure devotee is the greatest suffering.” That is the greatest, most intense separation.

His Holiness Jayapataka Swami,
Date: 2 Oct 1980
Place: New Orleans, USA""",True),
 ("""SQ123
Lord Caitanya is personification of mercy.
Lord Caitanya had advented for different purposes, but the extetrnal purpose was to spread the saṅkīrtana movement. The internal purpose was to experience the love of devotees for Kṛṣṇa, and naturally in the latter days in Jagannātha Purī, He was absorbed in the separation of the Lord. But if He showed that externally, the devotees may feel very sad. Although He was feeling that separation He didn’t show that externally.
His Holiness Jayapatākā Swami Mahārāja on 11 Dec 2022 in Śrī Māyāpur, India""",True),
 ("""SQ 123
someone may be an unalloyed devotee, may have a lot of piety, but if they not have the mercy of Lord Caitanya, then it is very hard for them to achieve prema.
>>> Ref. His Holiness Jayapatākā Swami Mahārāja on 17 Nov 2023 in Śrī Māyāpur, India""",True),

 ("""SQ 123        
Devotees neither interested in liberation nor impersonal feature, serving and pleasing Krsnā is their goal of life. 

HH Jayapataka Swami, on 11 Nov 2023 in Sri Mayapur""",True),
 ("""SQ 123
At the time of initiation one takes vows, promises that cannot be neglected.

His Holiness Jayapataka Swami on 21 Aug 2022 
in Hyderabad, India""", False),
("""SQ 123

At the time of initiation one takes vows, promises that cannot be neglected.

His Holiness Jayapataka Swami ,21 Aug 2022 ,Hyderabad, India""", False),
("""SQ 432 Devotees neither interested in liberation nor impersonal feature,serving and pleasing Krsnā is their goal of life. HH Jayapataka Swami, 11Nov 2023 Sridha Mayapur""",False),
("""SQ 181

Devotees neither interested in liberation nor impersonal feature, serving and pleasing Krsnā is their goal of life. HH Jayapataka Swami, 11Nov 2023 Sridham Mayapur
""", False),
("""SQ174
Lord Chaitanya he got people to chant Hare Krishna. As a result all kinds of secrets were reveal to the people. In this way krishna become fix in Everyone's consciousness           >>> Ref. His Holiness Jayapatākā Swami Mahārāja on 26th July 2023 Śrī Māyāpur, India """,False),

])



def test_Qoute_validty(qoute,status):
    qoute_object = QV.Qoute_validation(qoute)
    assert qoute_object.is_valid == status
