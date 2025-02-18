##
# @license
# Copyright 2018 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

# Node.js TensorFlow Binding config:
{
  'variables' : {
    'arch': '<!(node -p "process.arch")',
    'platform': '<!(node -p "process.platform")',
    'angle_lib_dir': '<(module_root_dir)/deps/angle/lib/<(platform)-<(arch)'
  },
  'targets' : [{
    'target_name' : 'nodejs_gl_binding_<(platform)_<(arch)',
    'sources' : [
      'binding/binding.cc',
      'binding/egl_context_wrapper.cc',
      'binding/webgl_extensions.cc',
      'binding/webgl_rendering_context.cc',
      'binding/webgl_sync.cc'
    ],
    'include_dirs' : [
      '..',
      '<(module_root_dir)/deps',
      '<(module_root_dir)/deps/angle/include'
    ],
    'conditions' : [
      [
        'OS=="linux"', {
          'libraries' : [
            '-Wl,-rpath,<@(angle_lib_dir)',
            '-lGLESv2',
            '-lEGL',
          ],
          'library_dirs' : ['<(angle_lib_dir)'],
        }
      ],
      [
        'OS=="mac"', {
          'libraries' : [
            '-Wl,-rpath,<@(angle_lib_dir)',
            '-lGLESv2',
            '-lEGL',
            '-lvk_swiftshader',
          ],
          'library_dirs' : ['<(angle_lib_dir)'],
          'include_dirs' : [
            '/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1/'
          ]
        }
      ],
      [
        'OS=="win"', {
          'defines': ['COMPILER_MSVC'],
          'libraries': ['libGLESv2', 'libEGL', 'vk_swiftshader'],
          'library_dirs' : ['<(angle_lib_dir)'],
          'copies': [
            {
              'destination': '<(PRODUCT_DIR)',
              'files': [
                '<(angle_lib_dir)/libEGL.dll',
                '<(angle_lib_dir)/libGLESv2.dll',
                '<(angle_lib_dir)/vulkan-1.dll',
                '<(angle_lib_dir)/vk_swiftshader.dll',
                '<(angle_lib_dir)/vk_swiftshader_icd.json'
              ]
            }
          ]
        },
      ]
    ]
  }]
}
