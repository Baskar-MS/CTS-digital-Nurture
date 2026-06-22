use college_db
db.createCollection("feedback")
{ ok: 1 }
db.getCollectionNames()
[ 'feedback' ]
db.feedback.insertMany([
{
  student_id: 1,
  course_code: "CS101",
  semester: "2022-ODD",
  rating: 5,
  comments: "Excellent teaching.",
  tags: ["challenging","well-structured"],
  submitted_at: new Date("2022-11-30T10:15:00Z"),
  attachments: [{filename:"notes.pdf",size_kb:240}]
},
{
  student_id: 2,
  course_code: "CS101",
  semester: "2022-ODD",
  rating: 4,
  comments: "Good examples.",
  tags: ["good-examples"],
  submitted_at: new Date("2022-11-28T09:00:00Z"),
  attachments: []
},
{
  student_id: 3,
  course_code: "CS101",
  semester: "2023-EVEN",
  rating: 3,
  comments: "Average course.",
  tags: ["moderate"],
  submitted_at: new Date("2023-04-10T11:00:00Z"),
  attachments: []
},
{
  student_id: 4,
  course_code: "CS102",
  semester: "2022-ODD",
  rating: 5,
  comments: "Very informative.",
  tags: ["excellent","practical"],
  submitted_at: new Date("2022-11-26T15:30:00Z"),
  attachments: []
},
{
  student_id: 5,
  course_code: "CS102",
  semester: "2023-EVEN",
  rating: 4,
  comments: "Useful content.",
  tags: ["well-structured"],
  submitted_at: new Date("2023-04-12T12:00:00Z"),
  attachments: []
},
{
  student_id: 6,
  course_code: "CS103",
  semester: "2022-ODD",
  rating: 2,
  comments: "Needs improvement.",
  tags: ["difficult"],
  submitted_at: new Date("2022-11-20T08:00:00Z"),
  attachments: []
},
{
  student_id: 7,
  course_code: "EC101",
  semester: "2022-ODD",
  rating: 1,
  comments: "Poor experience.",
  tags: ["hard"],
  submitted_at: new Date("2022-11-18T10:00:00Z"),
  attachments: []
},
{
  student_id: 8,
  course_code: "ME101",
  semester: "2023-EVEN",
  rating: 4,
  comments: "Interesting course.",
  tags: ["practical"],
  submitted_at: new Date("2023-04-15T14:00:00Z"),
  attachments: []
},
{
  student_id: 9,
  course_code: "CS103",
  semester: "2023-EVEN",
  rating: 5,
  comments: "Excellent explanations.",
  tags: ["excellent"],
  submitted_at: new Date("2023-04-18T16:00:00Z"),
  attachments: []
},
{
  student_id: 10,
  course_code: "CS101",
  semester: "2023-EVEN",
  rating: 4,
  comments: "Helpful instructor.",
  tags: ["good-examples","practical"],
  submitted_at: new Date("2023-04-20T10:00:00Z")
}
])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a3967dd6e7abb667b11c4dc'),
    '1': ObjectId('6a3967dd6e7abb667b11c4dd'),
    '2': ObjectId('6a3967dd6e7abb667b11c4de'),
    '3': ObjectId('6a3967dd6e7abb667b11c4df'),
    '4': ObjectId('6a3967dd6e7abb667b11c4e0'),
    '5': ObjectId('6a3967dd6e7abb667b11c4e1'),
    '6': ObjectId('6a3967dd6e7abb667b11c4e2'),
    '7': ObjectId('6a3967dd6e7abb667b11c4e3'),
    '8': ObjectId('6a3967dd6e7abb667b11c4e4'),
    '9': ObjectId('6a3967dd6e7abb667b11c4e5')
  }
}
db.feedback.countDocuments()
db.feedback.find({ rating: 5 })
{
  _id: ObjectId('6a3967dd6e7abb667b11c4dc'),
  student_id: 1,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent teaching.',
  tags: [
    'challenging',
    'well-structured'
  ],
  submitted_at: 2022-11-30T10:15:00.000Z,
  attachments: [
    {
      filename: 'notes.pdf',
      size_kb: 240
    }
  ]
}
{
  _id: ObjectId('6a3967dd6e7abb667b11c4df'),
  student_id: 4,
  course_code: 'CS102',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Very informative.',
  tags: [
    'excellent',
    'practical'
  ],
  submitted_at: 2022-11-26T15:30:00.000Z,
  attachments: []
}
{
  _id: ObjectId('6a3967dd6e7abb667b11c4e4'),
  student_id: 9,
  course_code: 'CS103',
  semester: '2023-EVEN',
  rating: 5,
  comments: 'Excellent explanations.',
  tags: [
    'excellent'
  ],
  submitted_at: 2023-04-18T16:00:00.000Z,
  attachments: []
}
db.feedback.find({
  course_code: "CS101",
  tags: "challenging"
})
{
  _id: ObjectId('6a3967dd6e7abb667b11c4dc'),
  student_id: 1,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent teaching.',
  tags: [
    'challenging',
    'well-structured'
  ],
  submitted_at: 2022-11-30T10:15:00.000Z,
  attachments: [
    {
      filename: 'notes.pdf',
      size_kb: 240
    }
  ]
}
db.feedback.find(
  {},
  {
    student_id: 1,
    course_code: 1,
    rating: 1,
    _id: 0
  }
)
{
  student_id: 1,
  course_code: 'CS101',
  rating: 5
}
{
  student_id: 2,
  course_code: 'CS101',
  rating: 4
}
{
  student_id: 3,
  course_code: 'CS101',
  rating: 3
}
{
  student_id: 4,
  course_code: 'CS102',
  rating: 5
}
{
  student_id: 5,
  course_code: 'CS102',
  rating: 4
}
{
  student_id: 5,
  course_code: 'CS102',
  rating: 4
}
{
  student_id: 6,
  course_code: 'CS103',
  rating: 2
}
{
  student_id: 7,
  course_code: 'EC101',
  rating: 1
}
db.feedback.updateMany(
  { rating: { $lt: 3 } },
  {
    $set: {
      needs_review: true
    }
  }
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}
db.feedback.find({ needs_review: true })

// 69. UPDATE: Add 'reviewed' tag to documents needing review
db.feedback.updateMany(
  { needs_review: true },
  {
    $push: {
      tags: "reviewed"
    }
  }
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}
db.feedback.find({
  tags: "reviewed"
})
{
  _id: ObjectId('6a3967dd6e7abb667b11c4e1'),
  student_id: 6,
  course_code: 'CS103',
  semester: '2022-ODD',
  rating: 2,
  comments: 'Needs improvement.',
  tags: [
    'difficult',
    'reviewed'
  ],
  submitted_at: 2022-11-20T08:00:00.000Z,
  attachments: [],
  needs_review: true
}
{
  _id: ObjectId('6a3967dd6e7abb667b11c4e2'),
  student_id: 7,
  course_code: 'EC101',
  semester: '2022-ODD',
  rating: 1,
  comments: 'Poor experience.',
  tags: [
    'hard',
    'reviewed'
  ],
  submitted_at: 2022-11-18T10:00:00.000Z,
  attachments: [],
  needs_review: true
}
db.feedback.deleteMany({
  semester: "2021-EVEN"
})
{
  acknowledged: true,
  deletedCount: 0
}
db.feedback.find({
  semester: "2021-EVEN"
})

db.feedback.countDocuments()
10
db.feedback.aggregate([
  {
    $match: {
      semester: "2022-ODD"
    }
  },
  {
    $group: {
      _id: "$course_code",
      avg_rating: {
        $avg: "$rating"
      },
      total_feedback: {
        $sum: 1
      }
    }
  },
  {
    $sort: {
      avg_rating: -1
    }
  }
])
{
  _id: 'CS102',
  avg_rating: 5,
  total_feedback: 1
}
{
  _id: 'CS101',
  avg_rating: 4.5,
  total_feedback: 2
}
{
  _id: 'EC101',
  avg_rating: 1,
  total_feedback: 1
}
db.feedback.aggregate([
  {
    $match: {
      semester: "2022-ODD"
    }
  },
  {
    $group: {
      _id: "$course_code",
      avg_rating: {
        $avg: "$rating"
      },
      total_feedback: {
        $sum: 1
      }
    }
  },
  {
    $project: {
      _id: 0,
      course_code: "$_id",
      average_rating: {
        $round: ["$avg_rating", 1]
      },
      total_feedback: 1
    }
  },
  {
    $sort: {
      average_rating: -1
    }
  }
])
{
  total_feedback: 1,
  course_code: 'CS102',
  average_rating: 5
}
{
  total_feedback: 2,
  course_code: 'CS101',
  average_rating: 4.5
}
{
  total_feedback: 1,
  course_code: 'CS103',
  average_rating: 2
}
{
  total_feedback: 1,
  course_code: 'EC101',
  average_rating: 1
}
db.feedback.aggregate([
  {
    $unwind: "$tags"
  },
  {
    $group: {
      _id: "$tags",
      tag_count: {
        $sum: 1
      }
    }
  },
  {
    $sort: {
      tag_count: -1
    }
  }
])
{
  _id: 'practical',
  tag_count: 3
}
{
  _id: 'good-examples',
  tag_count: 2
}
{
  _id: 'well-structured',
  tag_count: 2
}
{
  _id: 'excellent',
  tag_count: 2
}
{
  _id: 'reviewed',
  tag_count: 2
}
{
  _id: 'moderate',
  tag_count: 1
}
{
  _id: 'challenging',
  tag_count: 1
}
{
  _id: 'difficult',
  tag_count: 1
}
{
  _id: 'hard',
  tag_count: 1
}
db.feedback.createIndex({
  course_code: 1
})
// Verify index usage

db.feedback.find({
  course_code: "CS101"
}).explain("executionStats")
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'college_nosql.feedback',
    parsedQuery: {
      course_code: {
        '$eq': 'CS101'
      }
    },
    indexFilterSet: false,
    queryHash: '83CE04A5',
    planCacheShapeHash: '83CE04A5',
    planCacheKey: 'E4E1D11D',
    optimizationTimeMillis: 0,
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    prunedSimilarIndexes: false,
    winningPlan: {
      isCached: false,
      stage: 'FETCH',
      nss: 'college_nosql.feedback',
      inputStage: {
        stage: 'IXSCAN',
        nss: 'college_nosql.feedback',
        keyPattern: {
          course_code: 1
        },
        indexName: 'course_code_1',
        isMultiKey: false,
        multiKeyPaths: {
          course_code: []
        },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: {
          course_code: [
            '["CS101", "CS101"]'
          ]
        }
      }
    },
    rejectedPlans: []
  },
  executionStats: {
    executionSuccess: true,
    nReturned: 4,
    executionTimeMillis: 13,
    totalKeysExamined: 4,
    totalDocsExamined: 4,
    executionStages: {
      isCached: false,
      stage: 'FETCH',
      nReturned: 4,
      executionTimeMillisEstimate: 8,
      works: 5,
      advanced: 4,
      needTime: 0,
      needYield: 0,
      saveState: 0,
      restoreState: 0,
      isEOF: 1,
      nss: 'college_nosql.feedback',
      docsExamined: 4,
      alreadyHasObj: 0,
      inputStage: {
        stage: 'IXSCAN',
        nReturned: 4,
        executionTimeMillisEstimate: 8,
        works: 5,
        advanced: 4,
        needTime: 0,
        needYield: 0,
        saveState: 0,
        restoreState: 0,
        isEOF: 1,
        nss: 'college_nosql.feedback',
        keyPattern: {
          course_code: 1
        },
        indexName: 'course_code_1',
        isMultiKey: false,
        multiKeyPaths: {
          course_code: []
        },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: {
          course_code: [
            '["CS101", "CS101"]'
          ]
        },
        keysExamined: 4,
        seeks: 1,
        dupsTested: 0,
        dupsDropped: 0,
        peakTrackedMemBytes: 0
      }
    }
  },
  queryShapeHash: 'A93905E9C9869DA0264D6D85BC8875D4C698F973B857E2ABAAA6A355A5FCF0CB',
  command: {
    find: 'feedback',
    filter: {
      course_code: 'CS101'
    },
    '$db': 'college_nosql'
  },
  serverInfo: {
    host: 'BASKAR',
    port: 27017,
    version: '8.3.4',
    gitVersion: '4b03e7daaa316c78b9bf433046dba81637d581c0'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalQueryFrameworkControl: 'trySbeRestricted',
    internalQueryPlannerIgnoreIndexWithCollationForRegex: 1
  },
  ok: 1
}