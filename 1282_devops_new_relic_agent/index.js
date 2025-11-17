/**
 * New Relic Agent 프로젝트
 * 기본 진입점 파일
 */

console.log('🚀 Welcome to New Relic Agent!');
console.log('=' .repeat(50));

// 여기에 코드를 작성하세요
function init() {
    console.log('✅ New Relic Agent initialized successfully');
    console.log('📦 Ready to use!');
}

init();

// 예제 기능
function exampleFeature() {
    return {
        name: 'New Relic Agent',
        version: '1.0.0',
        status: 'active'
    };
}

console.log('📊 Project Info:', exampleFeature());
