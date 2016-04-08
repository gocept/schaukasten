module.exports = function (grunt) {
    "use strict";
    require('load-grunt-tasks')(grunt, {
        pattern: ['grunt-*', '!grunt-template-jasmine-istanbul']
    });

    grunt.config.init({
        clean: {
            release: [
                'frontend/dist',
            ]
        },
        babel: {
            options: {
                sourceMap: true
            },
            dist: {
                files: {
                    'frontend/js/app.base.js': 'frontend/src/app.base.js'
                }
            }
        },
        useminPrepare: {
            html: 'frontend/index.html',
            options: {
                dest: 'frontend/dist',
                flow: {
                    steps: {
                        template: ['concat'],
                        js: ['concat', 'uglifyjs'],
                        css: ['concat', 'cssmin']
                    },
                    post: {}
                }
            }
        },
        usemin: {
            html: ['frontend/dist/index.html'],
            options: {
                blockReplacements: {
                    template: function (block) {
                        return '<script src="' + block.dest + '" type="text/x-handlebars-template"></script>';
                    }
                }
            }
        },
        copy: {
            favicon: {
                src: './frontend/favicon.ico',
                dest: 'frontend/dist/favicon.ico',
            },
            index: {
                src: './frontend/index.html',
                dest: 'frontend/dist/index.html',
            },
        },
        filerev: {
            options: {
                encoding: 'utf8',
                algorithm: 'md5',
                length: 8
            },
            source: {
                files: [{
                    src: [
                        'frontend/dist/optimized.js',
                        'frontend/dist/optimized.min.css',
                    ]
                }]
            }
        },
        handlebars: {
            compile: {
                options: {
                    namespace: "ajja.templates",
                    processName: function (filePath) {
                        return filePath.split('/')[2].replace('.hbs', '');
                    }
                },
                files: {
                    "frontend/js/templates.js": "frontend/templates/*.hbs",
                }
            }
        },
        eslint: {
            target: ['frontend/src/app.base.js']
        },
        bower: {
            install: {
                options: {
                    copy: false
                }
            }
        },
        bower_concat: {
            all: {
                dest: 'frontend/js/bower.js',
            },
        },
        wiredep: {
            task: {
                src: [
                    'frontend/index.html'
                ],
                exclude: [
                    'frontend/bower_components/dropzone/dist/min/dropzone.min.css',
                    'frontend/bower_components/jasmine/lib/jasmine-core/jasmine.js',
                    'frontend/bower_components/jasmine-jquery/lib/jasmine-jquery.js'
                ],
                options: {
                }
            }
        },
        bump: {
            options: {
                files: ['bower.json', 'package.json', 'frontend/js/app.base.js',
                        'backend/src/schaukasten/version.json'],
                updateConfigs: [],
                commit: false,
                push: false,
                createTag: false,
                globalReplace: false,
                prereleaseName: 'dev',
                metadata: '',
                regExp: false
            }
        },
        jasmine : {
            schaukasten: {
                src : [
                    'frontend/js/app.base.js'
                ],
                options : {
                    specs : 'frontend/spec/javascripts/**/*.js',
                    vendor: ['frontend/js/bower.js', 'frontend/js/templates.js'],
                    styles: 'frontend/dist/optimized.min.*.css',
                    junit: {
                        path: process.env.CIRCLE_TEST_REPORTS + '/backend',
                        consolidate: true
                    },
                    template: require('grunt-template-jasmine-istanbul'),
                    templateOptions: {
                        coverage: 'coverage.json',
                        report: 'report'                    }
                },
            }
        },
        connect: {
            server: {
                options: {
                    port: 8888,
                    keepalive: true,
                    base: {
                        path: '.',
                        options: {
                            index: '_SpecRunner.html'
                        }
                    },
                    open: true
                }
            }
        }
    });
    grunt.registerTask('default', [
        'eslint',
        'babel',
        'handlebars:compile',
        'bower:install',
        'bower_concat:all',
        'wiredep:task'
    ]);
    grunt.registerTask('test', [
        'eslint',
        'babel',
        'jasmine:schaukasten:build',
        'connect',
    ]);
    grunt.registerTask('phantomjs', [
        'eslint',
        'babel',
        'jasmine:schaukasten'
    ]);
    grunt.registerTask('all', [
        'eslint',
        'clean',
        'babel',
        'handlebars:compile',
        'bower:install',
        'bower_concat:all',
        'copy',
        'wiredep:task',
        'useminPrepare',
        'concat:generated',
        'uglify:generated',
        'cssmin:generated',
        'filerev',
        'usemin',
    ]);
};
