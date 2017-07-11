{
  'targets': [{
    'target_name': 'cvc4',
    'sources': [
      'src/node-cvc4.cpp',
    ],
    'conditions': [
      ['OS=="linux"', {
        'defines': [
        ],
        'cflags_cc!': ['-fno-rtti', '-fno-exceptions'],
        'cflags_cc': [
          '-Wall',
          '-frtti',
          '-fexceptions',
        ],
        'libraries': [
          '-lcvc4', '-lcvc4parser'
        ]
      }]
    ]
  }]
}
