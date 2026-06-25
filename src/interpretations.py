SIGN_NAMES = {
    "Ari": "Bạch Dương", "Tau": "Kim Ngưu", "Gem": "Song Tử",
    "Can": "Cự Giải", "Leo": "Sư Tử", "Vir": "Xử Nữ",
    "Lib": "Thiên Bình", "Sco": "Bọ Cạp", "Sag": "Nhân Mã",
    "Cap": "Ma Kết", "Aqu": "Bảo Bình", "Pis": "Song Ngư",
}

SIGN_VI = {
    "Aries": "Bạch Dương", "Taurus": "Kim Ngưu", "Gemini": "Song Tử",
    "Cancer": "Cự Giải", "Leo": "Sư Tử", "Virgo": "Xử Nữ",
    "Libra": "Thiên Bình", "Scorpio": "Bọ Cạp", "Sagittarius": "Nhân Mã",
    "Capricorn": "Ma Kết", "Aquarius": "Bảo Bình", "Pisces": "Song Ngư",
}

PLANET_VI = {
    "Sun": "Mặt Trời", "Moon": "Mặt Trăng", "Mercury": "Sao Thủy",
    "Venus": "Sao Kim", "Mars": "Sao Hỏa", "Jupiter": "Sao Mộc",
    "Saturn": "Sao Thổ", "Uranus": "Sao Thiên Vương", "Neptune": "Sao Hải Vương",
    "Pluto": "Sao Diêm Vương",
}

ASPECT_VI = {
    "conjunction": "kết hợp với",
    "opposition": "đối nghịch với",
    "trine": "tam hợp với",
    "square": "vuông góc với",
    "sextile": "lục hợp với",
}

HOUSE_VI = {
    "First_House": "nhà 1 (bản thân)",
    "Second_House": "nhà 2 (tài chính)",
    "Third_House": "nhà 3 (giao tiếp)",
    "Fourth_House": "nhà 4 (gia đình)",
    "Fifth_House": "nhà 5 (sáng tạo)",
    "Sixth_House": "nhà 6 (công việc)",
    "Seventh_House": "nhà 7 (hôn nhân)",
    "Eighth_House": "nhà 8 (biến đổi)",
    "Ninth_House": "nhà 9 (triết lý)",
    "Tenth_House": "nhà 10 (sự nghiệp)",
    "Eleventh_House": "nhà 11 (bạn bè)",
    "Twelfth_House": "nhà 12 (tâm linh)",
}

PLANET_IN_SIGN = {
    "Sun": {
        "Cap": "Bản tính thực tế, kỷ luật, có trách nhiệm và tham vọng lớn. Thích kiểm soát và xây dựng sự nghiệp vững chắc.",
        "Ari": "Tính cách mạnh mẽ, tiên phong, dũng cảm. Luôn chủ động và không ngại đối đầu thử thách.",
    },
    "Moon": {
        "Tau": "Cảm xúc ổn định, trung thành, gắn bó với vật chất và sự an toàn. Ghét thay đổi đột ngột.",
        "Can": "Cảm xúc nhạy cảm, giàu tình cảm, gắn bó với gia đình. Nhu cầu được che chở và an toàn.",
    },
    "Mercury": {
        "Cap": "Tư duy thực tế, có kế hoạch, nói chuyện nghiêm túc và thẳng thắn. Học hỏi chậm mà chắc.",
        "Ari": "Tư duy nhanh nhạy, thẳng thắn, thích tranh luận. Quyết định nhanh nhưng dễ bốc đồng.",
    },
    "Venus": {
        "Aqu": "Yêu tự do, coi trọng tình bạn trong tình yêu. Cởi mở, phi truyền thống, thích sự độc đáo.",
        "Tau": "Yêu lãng mạn, chung thủy, thích sự xa hoa và ổn định. Ghen tuông nhẹ khi mất an toàn.",
    },
    "Mars": {
        "Cap": "Hành động có kỷ luật, kiên nhẫn, bền bỉ. Năng lượng tập trung vào sự nghiệp và mục tiêu dài hạn.",
        "Ari": "Hành động bốc đồng, quyết đoán, cạnh tranh. Luôn tràn đầy năng lượng và thích chinh phục.",
    },
}

PLANET_IN_HOUSE = {
    "Sun": {
        "Third_House": "Năng lượng dồn vào giao tiếp, học hỏi và kết nối xã hội. Có tài viết lách hoặc kinh doanh.",
        "Tenth_House": "Sự nghiệp và danh tiếng là trọng tâm cuộc đời. Thích làm lãnh đạo, được công nhận.",
    },
    "Moon": {
        "Seventh_House": "Cảm xúc gắn liền với quan hệ đối tác. Cần bạn đời đồng cảm và chia sẻ.",
        "Second_House": "Cảm xúc liên quan đến tiền bạc và giá trị vật chất. Dễ mua sắm theo cảm hứng.",
    },
    "Mercury": {
        "Fourth_House": "Tư duy hướng về gia đình và gốc rễ. Hay suy nghĩ về nhà cửa, quá khứ.",
        "Tenth_House": "Tư duy nhạy bén trong công việc. Có khả năng truyền đạt và giao tiếp tốt trong sự nghiệp.",
    },
    "Venus": {
        "Fourth_House": "Tình yêu với gia đình và mái ấm. Thích trang trí nhà cửa và cuộc sống nội tâm.",
        "Twelfth_House": "Tình yêu bí mật hoặc khuất lấp. Có xu hướng hy sinh trong tình cảm.",
    },
    "Mars": {
        "Fourth_House": "Xung đột gia đình hoặc động lực mạnh về nhà cửa. Năng lượng tập trung vào đời tư.",
        "Tenth_House": "Tham vọng nghề nghiệp lớn, cạnh tranh trong sự nghiệp. Có tố chất lãnh đạo.",
    },
}

TRANSIT_INTERP = {
    "Sun": {
        "conjunction": "Mặt Trời transit kết hợp sao natal: tăng cường năng lượng và sự tập trung vào lĩnh vực này.\nHôm nay bạn cảm thấy tràn đầy sinh lực, tự tin hơn về bản thân.",
        "opposition": "Mặt Trời transit đối nghịch: tạo ra sự căng thẳng giữa nhu cầu cá nhân và người khác.\nHãy lắng nghe quan điểm đối phương, tìm sự cân bằng thay vì khẳng định cái tôi.",
        "square": "Mặt Trời transit vuông góc: thử thách về bản ngã và hướng đi.\nCó thể gặp trở ngại hoặc xung đột — đây là cơ hội để điều chỉnh lại đường hướng.",
        "trine": "Mặt Trời transit tam hợp: năng lượng tích cực hỗ trợ cho bạn.\nMọi việc diễn ra suôn sẻ, tận dụng cơ hội để thể hiện bản thân.",
        "sextile": "Mặt Trời transit lục hợp: cơ hội nhẹ nhàng để phát triển.\nĐón nhận những đề nghị mới, chúng có lợi cho bạn.",
    },
    "Moon": {
        "conjunction": "Mặt Trăng transit kết hợp: cảm xúc dâng cao mãnh liệt.\nBạn nhạy cảm hơn bình thường — hãy chăm sóc cảm xúc của mình.",
        "opposition": "Mặt Trăng transit đối nghịch: xung đột cảm xúc với người khác.\nDễ hiểu lầm trong quan hệ, hãy nói rõ nhu cầu của bạn thay vì giữ trong lòng.",
        "square": "Mặt Trăng transit vuông góc: căng thẳng nội tâm.\nCảm xúc bất ổn, tránh quyết định quan trọng khi đang xúc động mạnh.",
        "trine": "Mặt Trăng transit tam hợp: cảm xúc hài hòa, dễ chịu.\nHôm nay là ngày tốt để kết nối với người thân và bạn bè.",
    },
    "Mercury": {
        "conjunction": "Sao Thủy transit kết hợp: tư duy và giao tiếp được tăng cường.\nĐầu óc minh mẫn, thích hợp để ký kết, học hỏi hay thuyết trình.",
        "opposition": "Sao Thủy transit đối nghịch: khó khăn trong giao tiếp.\nDễ hiểu lầm hoặc tranh cãi — hãy kiểm tra kỹ thông tin trước khi nói.",
        "square": "Sao Thủy transit vuông góc: tư duy bị cản trở.\nTránh ký hợp đồng quan trọng, dễ sai sót và hiểu nhầm.",
        "trine": "Sao Thủy transit tam hợp: tư duy thông suốt.\nGiao tiếp thuận lợi, ý tưởng dồi dào — ngày tốt để sáng tạo và học hỏi.",
        "sextile": "Sao Thủy transit lục hợp: cơ hội giao tiếp tích cực.\nCác cuộc trò chuyện mang lại lợi ích bất ngờ.",
    },
    "Venus": {
        "conjunction": "Sao Kim transit kết hợp: tình yêu và sắc đẹp lên ngôi.\nNgày lãng mạn, thích hợp hẹn hò, mua sắm hoặc làm đẹp.",
        "opposition": "Sao Kim transit đối nghịch: mâu thuẫn trong tình cảm.\nDễ bất đồng với người yêu hoặc bạn bè — hãy nhường nhịn và thấu hiểu.",
        "square": "Sao Kim transit vuông góc: thử thách trong các mối quan hệ.\nCảm xúc dễ bị tổn thương, không nên chi tiêu quá đà.",
        "trine": "Sao Kim transit tam hợp: tình cảm thuận lợi.\nHòa hợp với mọi người, tài chính tốt, cảm thấy yêu đời.",
        "sextile": "Sao Kim transit lục hợp: cơ hội tình cảm nhẹ.\nKết nối mới dễ chịu, có thể gặp người thú vị.",
    },
    "Mars": {
        "conjunction": "Sao Hỏa transit kết hợp: năng lượng dồi dào, quyết đoán.\nHành động mạnh mẽ, thích hợp để khởi xướng dự án mới.",
        "opposition": "Sao Hỏa transit đối nghịch: xung đột và đối đầu.\nDễ nổi nóng, hãy kiềm chế và tránh tranh cãi không cần thiết.",
        "square": "Sao Hỏa transit vuông góc: thách thức về hành động.\nDễ gặp chướng ngại, cần kiên nhẫn và kiểm soát cơn giận.",
        "trine": "Sao Hỏa transit tam hợp: năng lượng tích cực.\nHoàn thành việc nhanh chóng, thể thao và vận động tốt.",
        "sextile": "Sao Hỏa transit lục hợp: cơ hội hành động nhẹ.\nĐộng lực tăng, thích hợp để bắt đầu thói quen mới.",
    },
}


def sign_vn(sign_en):
    return SIGN_VI.get(sign_en, sign_en)


def planet_vn(name):
    return PLANET_VI.get(name, name)


def house_vn(house):
    return HOUSE_VI.get(house, house)


def interpret_natal_planet(planet, sign, house):
    lines = []
    sign_line = PLANET_IN_SIGN.get(planet, {}).get(sign, "")
    if sign_line:
        lines.append(sign_line)
    house_line = PLANET_IN_HOUSE.get(planet, {}).get(house, "")
    if house_line:
        lines.append(f"Ở {house_vn(house)}: {house_line}")
    return " ".join(lines)


def interpret_transit_aspect(tp, np, aspect, orb):
    vi_aspect = ASPECT_VI.get(aspect, aspect)
    lines = [f"Transit {PLANET_VI.get(tp, tp)} **{vi_aspect}** {PLANET_VI.get(np, np)} natal (sai số {orb:.1f}°)."]
    interp = TRANSIT_INTERP.get(tp, {}).get(aspect, "")
    if interp:
        lines.append(interp)
    return "\n".join(lines)


def summarize_star_sign(sign, asc_sign):
    desc = {
        "Cap": {
            "Lib": "Ma Kết với Thiên Bình mọc. Người thực tế, tham vọng nhưng biết cân bằng — ngoài lạnh trong nóng, có tài ngoại giao và kiên định với mục tiêu.",
        },
        "Ari": {
            "Gem": "Bạch Dương với Song Tử mọc. Năng động, thông minh, thích giao tiếp. Tiên phong trong công việc, linh hoạt trong ứng xử.",
        },
    }
    return desc.get(sign, {}).get(asc_sign,
        f"Mặt Trời ở {sign_vn(sign)}, Thiên Bình mọc {sign_vn(asc_sign)}.")


def summarize_day(planet, sign):
    summaries = {
        "Sun": {
            "Can": "Mặt Trời hôm nay ở Cự Giải — ngày của cảm xúc và gia đình. Bạn dễ nhạy cảm hơn, hướng về tổ ấm và những người thân yêu.",
        }
    }
    return summaries.get(planet, {}).get(sign,
        f"Hôm nay {PLANET_VI.get(planet, planet)} đi qua {sign_vn(sign)}.")


def get_aspect_outlook(aspects_list):
    hard = sum(1 for a in aspects_list if a["aspect"] in ("opposition", "square"))
    easy = sum(1 for a in aspects_list if a["aspect"] in ("trine", "sextile"))
    parts = []
    if hard > 0:
        parts.append(f"⚠️ {hard} góc chiêu thử thách (đối nghịch/vuông góc) — cần chú ý kiềm chế và linh hoạt.")
    if easy > 0:
        parts.append(f"✅ {easy} góc chiêu thuận lợi (tam hợp/lục hợp) — tận dụng cơ hội tốt.")
    return "\n".join(parts) if parts else ""
