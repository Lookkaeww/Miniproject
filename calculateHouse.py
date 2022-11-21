class calculatehouse:
    def housenumber(number):
        number = number.split("/")
        number = number[0] + number[1]
        cal_3 = str(number)
        if len(cal_3) == 1:
            cal_2 = int(cal_3)
        elif len(cal_3) == 2:
            cal_2 = int(cal_3[0])+int(cal_3[1])
        elif len(cal_3) == 3:
            cal_2 = int(cal_3[0])+int(cal_3[1])+int(cal_3[2])
        elif len(cal_3) == 4:
            cal_2 = int(cal_3[0])+int(cal_3[1])+int(cal_3[2])+int(cal_3[3])
        elif len(cal_3) == 5:
            cal_2 = int(cal_3[0])+int(cal_3[1])+int(cal_3[2])+int(cal_3[3])+int(cal_3[4])
        elif len(cal_3) == 6:
            cal_2 = int(cal_3[0])+int(cal_3[1])+int(cal_3[2])+int(cal_3[3])+int(cal_3[4])+int(cal_3[5])
        cal_5 = str(cal_2)
        if len(cal_5) == 1:
            cal_4 = int(cal_5)
        elif len(cal_5) != 1:
            cal_4 = int(cal_5[0])+int(cal_5[1])
        if cal_4 == 1:
            mes = "ผู้ที่อยู่อาศัยภายในบ้านหลังนี้มักมีความเป็นผู้นำสูง ใจร้อน กล้าคิดกล้าทำ แต่ว่าคนใจอ่อนชอบช่วยเหลือคนอื่น ๆ เลยทำให้มีเรื่องไม่สบายใจอยู่บ่อยครั้ง รวมทั้งผู้อยู่อาศัยจะมีลูกหลานเยอะ สมาชิกในบ้านมีหลายคน จะมีคนแวะเวียนมาหาอยู่ตลอดเวลา ส่วนหน้าที่การงานจะมีความเจริญรุ่งเรืองดี หากมีอาชีพรับราชการก็จะมีความก้าวหน้าในตำแหน่งหน้าที่การงาน มีผู้คนนับหน้าถือตา แต่ถ้าเป็นเจ้าของกิจการหรือนักธุรกิจก็สามารถประสบความสำเร็จได้ นอกจากนี้ หากบ้านมีพื้นที่กว้างขวาง ภายในบ้านปลูกต้นไม้ที่มีลักษณะลำต้นตรง เช่น “ไผ่” หรือ “มะพร้าว” จะช่วยส่งเสริมดวงชะตาผู้อยู่อาศัยมากยิ่งขึ้นอีกด้วย"
        elif cal_4 == 2:
            mes = "ผู้ที่อยู่อาศัยเป็นคนที่ชอบพบปะผู้คน ชอบเข้าสังคม และเป็นคนอบอุ่นจึงเป็นที่รักใคร่ของเพื่อนฝูงและมีเพื่อนมากพอสมควร แล้วยังเป็นคนที่มีเสน่ห์ แต่อ่อนไหวง่ายนะ ส่วนหน้าที่การงานของผู้ที่อยู่อาศัยในบ้านหลังนี้ก็ราบรื่นดี เหมาะกับการทำธุรกิจเกี่ยวกับน้ำ และความสวยความงาม หรือธุรกิจค้าขาย ร้านโชห่วย แต่ควรมีที่ปรึกษาหรือผู้ที่ทำธุรกิจร่วมกันจึงจะดี และข้อควรระวังคือปัญหาในเรื่องเงิน ๆ ทอง ๆ หรือเรื่องหนี้สิน อีกทั้งบ้านหลังนี้ควรตกแต่งบ้านด้วย “ตู้ปลา” หรือ “อ่างน้ำที่ประดับด้วยไม้น้ำ” และควรทำความสะอาดอยู่เสมอ หาก “บูชาเจ้าแม่กวนอิม” ด้วยแล้ว จะยิ่งทำให้ผู้อาศัยบ้านหลังนี้ประสบแต่ความสุขในชีวิตยิ่ง ๆ ขึ้นไป"
        elif cal_4 == 3:
            mes = "ผู้ที่อาศัยมักเป็นคนเฉลียวฉลาด มีคนยกย่องนับถือ แต่ก็เป็นคนใจร้อน ตรงไปตรงมา ชอบใช้กำลัง อาจจะมีเรื่องทะเลาเบาะแวงจนอาจจะถึงขึ้นโรงขึ้นศาล ผู้ที่อยู่อาศัยบ้านหลังนี้มักประสบแต่ความทุกข์ คนในบ้านเจ็บป่วยบ่อย และไม่ประสบความสำเร็จในเรื่องของการงาน หรือหากประกอบกิจการต่าง ๆ ก็มักจะล้มเหลวไม่รุ่งเรือง \n แต่อย่าเพิ่งกังวลไป! เราสามารถแก้เคล็ดได้ด้วยการ ตกแต่งด้วยวัสดุที่มี “สีทอง” หรือ “สีชมพู” ภายในบ้าน และประดับบ้านด้วยต้นไม้ที่มีกิ่งก้านแตกแขนงมาก เช่น “เฟื่องฟ้า” หรือ “มะม่วง” จะช่วยให้ดวงชะตาของผู้ที่อยู่อาศัยบ้านหลังนี้ดีขึ้นได้"
        elif cal_4 == 4:
            mes = "เป็นบ้านที่มีระดับความเป็นมงคลสูง ส่งผลให้คนในบ้านมั่งคั่ง ประสบความสำเร็จ มีเกียรติยศชื่อเสียง มีผู้คนไปมาหาสู่เสมอ ผู้ที่อยู่อาศัยมักเป็นคนช่างพูด ช่างเจรจา ชอบในเรื่องการติดต่อสื่อสาร มีสติปัญญาแหลมคม แต่ขาดความระมัดระวังรอบคอบและความอดทน ดังนั้นต้องระวังเรื่องนี้ให้ดี และบ้านหลังนี้ยังเป็นบ้านที่ดีให้โชคลาภแก่ผู้ที่อยู่อาศัย ลูกหลานมีการศึกษาที่ดี แถมยังเหมาะกับผู้ที่ประกอบอาชีพค้าขายอีกด้วย หากมีกิจการที่รุ่งเรืองดี แต่ให้ระวังเรื่องสุขภาพที่เกี่ยวกับลำไส้และกระเพาะอาหาร \n ผู้ที่อยู่อาศัยในบ้านหลังนี้ต้องเสริมดวงชะตาให้เฮง ๆ ปัง ๆ ยิ่งขึ้นไปอีก ควรตกแต่งบ้านด้วยต้นไม้ที่มีกลิ่นหอมเย็น ๆ เช่น “ต้นโมก”, “หมาก” หรือ “ชมพู่” ส่วนภายในบ้านควรตกแต่งด้วย “สีเขียว”, “รูปภาพธรรมชาติ”, “เลี้ยงปลา” หรือ “เลี้ยงนก” จะทำให้เสริมดวงชะตาดีขึ้นไปอีก"
        elif cal_4 == 5:
            mes = "ผู้ที่อยู่อาศัยมักเป็นที่รักของญาติมิตรและเพื่อนบ้อง อีกทั้งยังเป็นคนที่มีเสน่ห์ ชอบช่วยเหลือผู้อื่นเสมอ ๆ แต่บางทีก็มากเกินไป จนนำพาแต่ความทุกข์มาให้ มีเรื่องเดือนเนื้อร้อนใจอยู่บ่อยครั้ง ถือว่าเป็นข้อเสียของคนที่อาศัยบ้านหลังนี้เลย แต่เลข 5 ก็ถือเป็นเลขที่ดี เหมาะสำหรับผู้ที่ประกอบอาชีพ ครูอาจารย์ จะทำให้มีคนเคารพ นับหน้าถือตา แต่ถ้าทำธุรกิจก็จะประสบความสำเร็จเจริญรุ่งเรืองได้เหมือนกัน \n ดังนั้นการตกแต่งบ้านด้วย “สีขาว” จะทำให้บ้านดูสง่า สวยงาม และให้ความร่มเย็น ห้องรับแขกควรตกแต่งด้วย “เกียรติบัตร”, “ถ้วยรางวัล”, “ภาพแห่งความสำเร็จต่าง ๆ” และ “บูชาสิ่งศักดิ์สิทธิ์” ที่บูชานับถือ จะช่วยส่งเสริมให้บ้านเป็นมงคลมากยิ่งขึ้น"
        elif cal_4 == 6:
            mes = "ผู้ที่อยู่อาศัยเป็นคนที่มีเสน่ห์ เป็นที่รักของผู้คนมากมาย มักมีผู้หลักผู้ใหญ่ให้การเกื้อหนุนอยู่เสมอ แต่เป็นคนใช้ค่อนข้างใช้จ่ายฟุ่มเฟือย แต่บ้านหลังนี้ก็เป็นบ้านที่ดีนะ เหมาะสำหรับผู้ที่ประกอบอาชีพค้าขาย หรือเป็นเจ้าของกิจการ โดยเฉพาะกิจการเกี่ยวกับอาหาร เครื่องดื่ม เครื่องใช้ไฟฟ้า จะยิ่งเจริญรุ่งเรือง เงินทองไหลมาเทมา ประสบความสำเร็จเป็นอย่างมาก \n อีกทั้งการปลูกต้นไม้ที่มีกลิ่นหอม เช่น “โมก”, “แก้ว” และ “กุหลาบ” จะช่วยให้เสริมดวงชะตาผู้อยู่อาศัยให้ดียิ่งขึ้นไปอีก แต่ข้อควรควรระวังคือเรื่องของสุขภาพที่เกี่ยวกับ หัวใจ ไขมันในเลือด หรือโรคทางเพศ ต้องหมั่นรักษาสุขภาพด้วยนะ \n แก้เคล็ดเสริมดวงให้ดียิ่งขึ้นด้วยการ จัดบ้านให้เป็นระเบียบเรียบร้อย อย่าปล่อยให้สกปรก และควรตกแต่งบ้านด้วย “ไม้”,“ของตกแต่งที่มีสีน้ำตาล” หรือ “สีอิฐธรรมชาติ” ควรปลูกต้นไม้ให้ร่มรื่นมากกว่าหลังอื่น ๆ จะช่วยทำให้บ้านเป็นมงคลมากยิ่งขึ้น ลองเอาไปปรับเปลี่ยนกันได้นะ"
        elif cal_4 == 7:
            mes = "ผู้ที่อยู่อาศัยมักเป็นคนหนักแน่น และเป็นคนมีเคราะห์กรรม เพราะเลข 7 เป็นเลขของอุปสรรค ทำให้ผู้ที่อยู่อาศัยภายในบ้านหลังนี้มักพบเจอกับอุปสรรคมากมาย กว่าที่จะประสบความสำเร็จ และยังมีปัญหาในเรื่องของความขัดแย้งภายในครอบครัวอีก หากมีลูกน้องก็มักจะไม่ซื่อสัตย์ ทำให้ชีวิตไม่ค่อยมีความสุขสงบเท่าไหร่ และอาจมีเคราะห์กรรมถึงขั้นเลือดตกยางออกด้วย ดังนั้นผู้ที่อยู่อาศัยภายในบ้านหลังนี้ไม่ควรอยู่ติดที่ ควรเดินทางอยู่เสมอ เช่น ไกด์นำเที่ยว แอร์โฮสเตท"
        elif cal_4 == 8:
            mes = "ผู้ที่อยู่อาศัยควรเป็นคนที่กล้าตัดสินใจและมีสติอยู่เสมอ ไม่ลุ่มหลงอยู่ในกิเลส เพราะจะทำให้มีแต่ความทุกข์ใจ บ้านหลังนี้จะดีหรือไม่ดีขึ้นอยู่กับดวงชะตาของผู้ที่อยู่อาศัยเอง แต่ถ้าคนดวงแข็ง และอยู่ในช่วงดวงดีก็จะทำให้ส่งผลแต่เรื่องดี ๆ แต่ถ้าไม่ใช่คนดวงแข็งหรืออยู่ในช่วงดวงตกก็จะพบแต่ความทุกข์หนัก อาจจะมีเคราะห์เกี่ยวกับอุบัติเหตุ อาจถึงขั้นสูญเสียเลย ส่วนเรื่องเงินทองก็ไม่ดี เพราะจะมีเหตุให้ต้องเสียเงินเสียทองอยู่เสมอ \n ดังนั้นควรแก้เคล็ดโดยการตกแต่งบ้านด้วย “ภาพสิ่งศักดิ์สิทธิ์” หรือ “ภาพที่เป็นมงคล” และตกแต่งบ้านให้มีความสว่างไสวอยู่เสมอ จะช่วยทำให้บ้านหลังนี้เป็นมงคลมากยิ่งขึ้น"
        elif cal_4 == 9:
            mes = "ผู้อาศัยมักเป็นคนที่มีอำนาจบารมี มีคนความเคารพ นับหน้าถือตาอยู่เสมอ เลข 9 นั้นเป็นเลขที่เป็นมงคลมาก เป็นเลขของคุณงามความดี ไม่ว่าจะทำอะไรก็จะมีคนคอยเกื้อหนุนรับใช้อยู่เสมอ ผู้ที่อยู่อาศัยบ้านหลังนี้มักมีอายุยืนยาว หากทำธุรกิจหรือกิจการของตนเองก็จะประสบความสำเร็จ มีกิจการใหญ่โตเลยทีเดียว แต่ถ้าผู้อยู่อาศัยมีอาชีพที่ไม่สุจริต ผิดกฎหมาย จะให้ได้รับกรรมหนักมากกว่าคนอื่น ๆ หลายเท่า \n ดังนั้นควรตกแต่งบ้านด้วยไม้มงคลต่าง ๆ อย่าง “ไผ่กวนอิม” หรือ “โป๊ยเซียน” และควรจัดบ้านให้ดูสะอาดตา โปร่ง โล่ง สบาย จะช่วยให้บ้านเป็นมงคลมากยิ่งขึ้นด้วย"
        return cal_4, mes