#ifndef DEFINEVALUEHELPER_H
#define DEFINEVALUEHELPER_H

#define READ_NAME(valueName) valueName

#define WRITE_NAME(valueName) \
    set_##valueName

#define INIT_NAME(valueName) \
    init_##valueName

#define NOTIFY_NAME(valueName) \
    valueName##Changed

#define DEFINE_VALUE(type, valueName, defaultValue) \
Q_PROPERTY(type valueName READ READ_NAME(valueName) WRITE WRITE_NAME(valueName) NOTIFY NOTIFY_NAME(valueName)) \
public: \
    type READ_NAME(valueName)() const { return m_##valueName; } \
    void WRITE_NAME(valueName)(type valueName) { \
        if(valueName == m_##valueName) { \
            return; \
        } \
        m_##valueName = valueName; \
        emit NOTIFY_NAME(valueName)(); \
    } \
Q_SIGNALS: \
    void NOTIFY_NAME(valueName)(); \
private: \
    type m_##valueName = defaultValue;

#endif // DEFINEVALUEHELPER_H
