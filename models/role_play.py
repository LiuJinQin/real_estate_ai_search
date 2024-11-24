class RolePlay:
    def greeting_stage(self, user_input):
        # 问候阶段
        return "您好！我是您的房产中介顾问，请问您有什么需求？"

    def collect_requirements_stage(self, user_input):
        # 收集需求阶段
        # 假设在此阶段收集用户的预算、位置和房产类型偏好等信息
        return "好的，能否告诉我您的预算、理想的位置和房产类型呢？"

    def recommendation_stage(self, user_input, requirements):
        # 推荐阶段，根据用户需求推荐房源
        # 通过Text2SQL生成查询结果，这里仅作为示例
        properties = [
            "Remuera的独立别墅，三房两浴，售价120万",
            "Newmarket的公寓，两房一浴，售价85万"
        ]
        return f"根据您的需求，我推荐以下房源：\n" + "\n".join(properties)

    def follow_up_stage(self, user_input):
        # 跟进反馈阶段
        return "您对这些房源有什么想法？是否需要我安排实地看房？"

    def should_end_dialogue(self, user_input):
        # 检查用户输入是否表明结束对话
        end_phrases = ["谢谢", "不需要了", "再见"]
        return any(phrase in user_input for phrase in end_phrases)
