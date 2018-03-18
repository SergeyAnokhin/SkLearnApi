from ApiPresentor import ApiPresentor

presentor = ApiPresentor()

### INIT ###
presentor.configure({
    'all_events': ['Event1', 'Event2', 'Event3'],
    'events_window': 600,
    'epoch_step': 30
})

### TRAIN ###
presentor.addTrainData({
    'header': {
        'datetime': '2018-03-18T15:16:00', 'duration': 600,
        'className': 'class1', 'comment': ''
    },
    'events': [
        [ 10, 'Event1' ],
        [ 100, 'Event1' ],
        [ 110, 'Event1' ],
        [ 200, 'Event2' ],
        [ 300, 'Event3' ]
    ]
})
presentor.addTrainData({
    'header': {
        'datetime': '2018-04-18T15:16:00', 'duration': 600,
        'className': 'class2', 'comment': ''
    },
    'events': [
        [ 10, 'Event1' ],
        [ 100, 'Event1' ],
        [ 110, 'Event2' ],
        [ 200, 'Event2' ],
        [ 300, 'Event3' ]
    ]
})
presentor.addTrainData({
    'header': {
        'datetime': '2018-05-18T15:16:00', 'duration': 600,
        'className': 'class3', 'comment': ''
    },
    'events': [
        [ 10, 'Event1' ],
        [ 100, 'Event1' ],
        [ 110, 'Event3' ],
        [ 200, 'Event2' ],
        [ 300, 'Event3' ]
    ]
})
presentor.fit();

### PREDICT ###
prediction = presentor.predict({
    'header': {
        'datetime': '2018-05-18T15:16:00', 'duration': 600,
        # 'className': 'class3', 'comment': ''
    },
    'events': [
        [ 10, 'Event1' ],
        [ 100, 'Event1' ],
        [ 110, 'Event3' ],
        [ 200, 'Event2' ],
        [ 300, 'Event3' ]
    ]
})

### DISPLAY ###
print(prediction)